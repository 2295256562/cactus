from django.db import models
from utils.model_base import ModelWithName, ModelWithKey, ModelWithDesc, ModelWithUser, NULLABLE, NULLABLE_FK


class Project(ModelWithDesc):
    class Meta:
        verbose_name_plural = verbose_name = '项目'


class Env(ModelWithName):
    class Meta:
        verbose_name_plural = verbose_name = '环境'
    project = models.ForeignKey(Project, verbose_name='项目', on_delete=models.CASCADE)
    domain = models.CharField('域名', max_length=500)


class EnvVariable(ModelWithKey):
    class Meta:
        verbose_name_plural = verbose_name = '环境变量'

    env = models.ForeignKey(Env, verbose_name='环境', on_delete=models.CASCADE)
    value = models.CharField('变量值', max_length=200)


class EnvHeader(ModelWithKey):
    class Meta:
        verbose_name_plural = verbose_name = '请求头配置'

    env = models.ForeignKey(Env, verbose_name='环境', on_delete=models.CASCADE)
    value = models.CharField('变量值', max_length=200)


class Tag(ModelWithDesc):
    class Meta:
        verbose_name_plural = verbose_name = '标签'
    project = models.ForeignKey(Project, verbose_name='项目', on_delete=models.CASCADE)
