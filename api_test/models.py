import os

import requests
import yaml
from logz import log
from django.db import models

from utils.model_base import ModelBase, ModelWithName, ModelWithKey, ModelWithDesc, NULLABLE, NULLABLE_FK


def yaml2dict(text, default={}):
    try:
        return yaml.safe_load(text)
    except Exception as ex:
        log.exception(ex)
        return default


class Project(ModelWithDesc):
    class Meta:
        verbose_name_plural = verbose_name = '项目'


class Env(ModelWithName):
    class Meta:
        verbose_name_plural = verbose_name = '环境'
    project = models.ForeignKey(Project, verbose_name='项目', on_delete=models.CASCADE)
    base_url = models.CharField('域名', max_length=500, **NULLABLE)
    request = models.TextField('请求more配置', **NULLABLE)


class Variable(ModelWithKey):
    class Meta:
        verbose_name_plural = verbose_name = '环境变量'
    VALUE_TYPE_CHOICES = (
        ('string', '字符串'),
        ('number', '数字'),
        ('yaml', 'yaml'),
        ('expr', 'Python表达式'),
    )
    project = models.ForeignKey(Project, verbose_name='项目', related_name='project_variables', on_delete=models.CASCADE)
    env = models.ForeignKey(Env, verbose_name='环境', related_name='env_variables', **NULLABLE_FK)
    # value_type = models.CharField('变量类型', max_length=12, default='string')
    value = models.CharField('变量值', max_length=500)   # yaml string


class Tag(ModelWithDesc):
    class Meta:
        verbose_name_plural = verbose_name = '标签'
    project = models.ForeignKey(Project, verbose_name='项目', on_delete=models.CASCADE)


class ApiCategory(ModelWithDesc):
    class Meta:
        verbose_name_plural = verbose_name = '接口分类'
    project = models.ForeignKey(Project, verbose_name='项目', on_delete=models.CASCADE)


class Api(ModelWithDesc):
    class Meta:
        verbose_name_plural = verbose_name = '接口'

    METHOD_CHOICES = (
        ('get', 'GET'),
        ('post', 'POST'),
        ('put', 'PUT'),
        ('delete', 'DELETE'),
        ('head', 'HEAD'),
        ('patch', 'PATCH'),
        ('options', 'OPTIONS'),
    )

    project = models.ForeignKey(Project, verbose_name='项目', on_delete=models.CASCADE)
    category = models.ForeignKey(ApiCategory, verbose_name='接口组', **NULLABLE_FK)
    path = models.CharField('接口路径', max_length=200)
    method = models.CharField('请求方法', max_length=10, choices=METHOD_CHOICES, default='get')


class TestCase(ModelWithKey):
    class Meta:
        verbose_name_plural = verbose_name = '测试用例'
    project = models.ForeignKey(Project, verbose_name='项目', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, verbose_name='标签', **NULLABLE_FK)

    def run(self, session=None, context=None, env_id=None, debug=False):
        for step in self.steps.objects.all().order_by('order'):
            step.run(session, context, env_id, debug)


class TestStep(ModelWithDesc):
    class Meta:
        verbose_name_plural = verbose_name = '测试步骤'
    case = models.ForeignKey(TestCase, verbose_name='测试用例', related_name="steps", on_delete=models.CASCADE)
    order = models.IntegerField('步骤顺序')
    api = models.ForeignKey(Api, verbose_name='接口', on_delete=models.CASCADE)
    skip = models.BooleanField('跳过用例', default=False)
    request = models.TextField('请求数据')
    extract = models.TextField('提取数据')
    check = models.TextField('断言数据')

    def run(self, session=None, context=None, env_id=None, debug=False):
        session = session or requests.session()
        context = context or os.environ
        if env_id:
            env = Env.objects.get(id=env_id, project=self.case.project)
            if env:  # todo schema校验
                base_url = env.base_url
                request_conf = yaml2dict(env.request)
                variables = {obj.key: yaml2dict(obj.value) for obj in env.env_variables.objects.all()}
                context.update(variables)
                for key, value in request_conf.items():
                    setattr(session, key, value)
        url = self.api.url
        if base_url and not url.startswith('http'):
            url = '/'.join((base_url.rstrip('/'), self.url.lstrip('/')))
        request = yaml2dict(self.request)
        request.update(dict(url=url, method=self.api.method))   # todo 调整优先级
        log.info(f'发送请求: {request}')
        try:
            response = session.request(**request)
        except Exception as ex:
            log.exception(ex)
        else:
            log.info(f'响应数据: {response.text}')


class TestSuite(ModelWithDesc):
    class Meta:
        verbose_name_plural = verbose_name = '测试套件'
    project = models.ForeignKey(Project, verbose_name='项目', on_delete=models.CASCADE)
    suite = models.ForeignKey('self', verbose_name='父级套件', related_name='sub_suites', **NULLABLE_FK)
    testcases = models.ManyToManyField(TestCase, verbose_name='测试用例', blank=True)

    def run(self, session=None, context=None, env_id=None, debug=False):
        for case in self.testcases.objects.all():
            case.run(session, context, env_id, debug)
        for suite in self.sub_suites.objects.all():
            suite.run(session, context, env_id, debug)


class TestReport(ModelWithDesc):
    class Meta:
        verbose_name_plural = verbose_name = '测试步骤'
    project = models.ForeignKey(Project, verbose_name='项目', on_delete=models.CASCADE)
    suite = models.ForeignKey(TestSuite, verbose_name='测试套件', **NULLABLE_FK)
    case = models.ForeignKey(TestCase, verbose_name='测试用例', **NULLABLE_FK)
    step = models.ForeignKey(TestStep, verbose_name='测试步骤', **NULLABLE_FK)
    content = models.TextField('报告内容')
