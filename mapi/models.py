from django.db import models

from utils.model_base import ModelBase, ModelWithName, ModelWithKey, ModelWithDesc, ModelWithUser, NULLABLE, NULLABLE_FK


class ProjectGroup(ModelWithDesc):
    class Meta:
        verbose_name_plural = verbose_name = '项目组'


class Project(ModelWithDesc):
    class Meta:
        verbose_name_plural = verbose_name = '项目'
    group = models.ForeignKey(ProjectGroup, verbose_name='项目', on_delete=models.CASCADE)


class Env(ModelWithName):
    class Meta:
        verbose_name_plural = verbose_name = '环境'
    project = models.ForeignKey(Project, verbose_name='项目', on_delete=models.CASCADE)
    domain = models.CharField('域名', max_length=500)


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
    DATA_TYPE_CHOICES = (
        ('none', '无'),
        ('form', '表单'),
        ('json', 'JSON'),
        ('raw', '原始'),
        ('multipart', '复合表单'),
        ('binary', '二进制'),
    )

    project = models.ForeignKey(Project, verbose_name='项目', on_delete=models.CASCADE)
    category = models.ForeignKey(ApiCategory, verbose_name='接口组', **NULLABLE_FK)
    path = models.CharField('接口路径', max_length=200)
    method = models.CharField('请求方法', max_length=10, choices=METHOD_CHOICES, default='get')


class ApiDoc(ModelBase):
    class Meta:
        verbose_name_plural = verbose_name = '接口文档'
    api = models.OneToOneField(Api, verbose_name='接口', on_delete=models.CASCADE)
    markdown = models.TextField('内容', default='')
 
    def __str__(self):
        return self.api.name + '接口文档'
