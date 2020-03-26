import os
import sys
from string import Template
from collections import ChainMap

import requests
import yaml
from logz import log
from django.db import models

from utils.model_base import ModelBase, ModelWithName, ModelWithKey, ModelWithDesc, NULLABLE, NULLABLE_FK
from utils.runner import yaml2dict, render, run_step


class Project(ModelWithDesc):
    class Meta:
        verbose_name_plural = verbose_name = '项目'


class Env(ModelWithName):
    class Meta:
        verbose_name_plural = verbose_name = '环境'
    project = models.ForeignKey(Project, verbose_name='项目', on_delete=models.CASCADE)
    base_url = models.CharField('域名', max_length=500, **NULLABLE)
    request = models.TextField('请求默认配置', **NULLABLE)

    def parse(self):
        base_url = self.base_url
        variables = {obj.key: obj.value for obj in self.env_variables.all()}  # todo 类型判断
        config = dict(base_url=base_url, request=yaml2dict(self.request), variables=variables)
        return config


class Variable(ModelWithKey):
    class Meta:
        verbose_name_plural = verbose_name = '变量'
    VALUE_TYPE_CHOICES = (
        ('string', '字符串'),
        ('number', '数字'),
        ('yaml', 'yaml'),
        ('expr', 'Python表达式'),
    )
    project = models.ForeignKey(Project, verbose_name='项目', related_name='project_variables', on_delete=models.CASCADE)
    env = models.ForeignKey(Env, verbose_name='环境', related_name='env_variables', **NULLABLE_FK)
    # value_type = models.CharField('变量类型', max_length=12, default='string')


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


class TestCase(ModelWithDesc):
    class Meta:
        verbose_name_plural = verbose_name = '测试用例'
    project = models.ForeignKey(Project, verbose_name='项目', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, verbose_name='标签', blank=True)


    def parse(self, context=None, env_id=None):
        data = dict(name=self.name, description=self.description)
        data['tags'] = [tag.name for tag in self.tags.all()]
        if env_id:
            env = Env.objects.get(id=env_id, project=self.project)
            if env:  # todo schema校验
                data['config'] = env.parse()
        data['steps'] = [step.parse() for step in self.steps.all()]
        return data


    def run(self, session=None, context=None, env_id=None, debug=False):
        result = dict(name=self.name, status='PASS')
        steps = self.steps.all().order_by('order')
        step_results = []
        for step in steps:
            step_results.append(step.run(session, context, env_id, debug))
        is_pass = all([step['status'] == 'PASS' for step in step_results])
        result['status'] = 'PASS' if is_pass else 'FAIL'
        result['steps'] = step_results
        return result


    def copy(self):
        case = self
        new_case = TestCase.objects.create(name=case.name, description=case.description, project=case.project)
        [new_case.tags.add(tag) for tag in case.tags.all()]
        for step in case.steps.all():
            TestStep.objects.create(name=step.name, description=step.description, case=new_case,
                                    order=step.order, api=step.api, skip=step.skip, request=step.request,
                                    extract=step.extract, check=step.check)

class TestStep(ModelWithDesc):
    class Meta:
        verbose_name_plural = verbose_name = '测试步骤'
    case = models.ForeignKey(TestCase, verbose_name='测试用例', related_name="steps", on_delete=models.CASCADE)
    order = models.IntegerField('步骤顺序')
    api = models.ForeignKey(Api, verbose_name='接口', on_delete=models.CASCADE)
    skip = models.BooleanField('跳过用例', default=False)
    request = models.TextField('请求数据')
    extract = models.TextField('提取数据', **NULLABLE)
    check = models.TextField('断言数据', **NULLABLE)


    def parse(self, context=None, env_id=None):
        context = context or ChainMap({}, os.environ)
        data = dict(name=self.name, skip=self.skip, extract=yaml2dict(self.extract), check=yaml2dict(self.check))
        url = self.api.path

        if env_id:
            env = Env.objects.get(id=env_id, project=self.case.project)
            if env:  # todo schema校验
                data['config'] = env.parse()

        request = dict(method=self.api.method, url=url)
        request_str = self.request
        if '$' in request_str:
            request_str = render(request_str, context)
        request.update(yaml2dict(request_str))

        data['request'] = request
        return data


    def run(self, session=None, context=None, env_id=None, debug=False):  #todo move to utils
        data = self.parse(context, env_id)
        result = run_step(data, session, context, debug)
        return result

    def copy(self):
        step = self
        TestStep.objects.create(name=step.name, description=step.description, case=step.case,
                                order=step.order + 1, api=step.api, skip=step.skip, request=step.request,
                                extract=step.extract, check=step.check)


class TestSuite(ModelWithDesc):
    class Meta:
        verbose_name_plural = verbose_name = '测试套件'
    project = models.ForeignKey(Project, verbose_name='项目', on_delete=models.CASCADE)
    suite = models.ForeignKey('self', verbose_name='父级套件', related_name='sub_suites', **NULLABLE_FK)
    testcases = models.ManyToManyField(TestCase, verbose_name='测试用例', blank=True)


    def parse(self, context=None, env_id=None):
        data = dict(name=self.name, description=self.description)
        if env_id:
            env = Env.objects.get(id=env_id, project=self.project)
            if env:  # todo schema校验
                data['config'] = env.parse()

        data['testcases'] = [case.parse(env_id=env_id) for case in self.testcases.all()]  # todo sub_suites
        return data


    def run(self, session=None, context=None, env_id=None, debug=False):
        results = []
        for case in self.testcases.all():
            results.append(case.run(session, context, env_id, debug))
        for suite in self.sub_suites.all():
            results.extend(suite.run_step(session, context, env_id, debug))
        TestReport.objects.create(name=f'{self.name}测试报告', project=self.project, suite=self, content=results)
        return dict(results=results)

    def copy(self):
        suite = self
        new_suite = TestSuite.objects.create(name=suite.name, description=suite.description,
                                             project=suite.project)
        [new_suite.testcases.add(case) for case in suite.testcases.all()]


class TestReport(ModelWithDesc):
    class Meta:
        verbose_name_plural = verbose_name = '测试报告'
    project = models.ForeignKey(Project, verbose_name='项目', on_delete=models.CASCADE)
    suite = models.ForeignKey(TestSuite, verbose_name='测试套件', **NULLABLE_FK)
    case = models.ForeignKey(TestCase, verbose_name='测试用例', **NULLABLE_FK)
    step = models.ForeignKey(TestStep, verbose_name='测试步骤', **NULLABLE_FK)
    content = models.TextField('报告内容')


# class AgentGroup(ModelWithDesc):
#     class Meta:
#         verbose_name_plural = verbose_name = '执行节点组'
#
#     project = models.ForeignKey(Project, verbose_name='项目', on_delete=models.CASCADE)
#     env = models.ForeignKey(Env, verbose_name='环境', related_name='env_agents', **NULLABLE_FK)
#     suite = models.ForeignKey(TestSuite, verbose_name='测试套件', related_name='suite_agents', **NULLABLE_FK)
#     schedule = models.CharField('执行计划', max_length=100)


class Agent(ModelWithDesc):
    class Meta:
        verbose_name_plural = verbose_name = '执行节点'

    project = models.ForeignKey(Project, verbose_name='项目', on_delete=models.CASCADE)
    # group = models.ForeignKey(AgentGroup, verbose_name='节点组', **NULLABLE_FK)
    env = models.ForeignKey(Env, verbose_name='环境', related_name='env_agents', **NULLABLE_FK)

    suite = models.ForeignKey(TestSuite, verbose_name='测试套件', related_name='suite_agents', **NULLABLE_FK)

    ip = models.CharField('IP', max_length=100)
    active = models.BooleanField('活动', default=False)
    schedule = models.CharField('执行计划', max_length=100)

