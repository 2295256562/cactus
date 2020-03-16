from django.db import models
from utils.model_base import ModelBase, ModelWithName, ModelWithKey, ModelWithDesc, ModelWithUser, NULLABLE, NULLABLE_FK

from projects.models import Project


class ApiGroup(ModelWithDesc):
    class Meta:
        verbose_name_plural = verbose_name = '接口组'
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

    group = models.ForeignKey(ApiGroup, verbose_name='接口组', on_delete=models.CASCADE)
    path = models.CharField('接口路径', max_length=200)
    method = models.CharField('请求方法', max_length=10, choices=METHOD_CHOICES, default='get')
    data_type = models.CharField('内容类型', max_length=15, choices=DATA_TYPE_CHOICES, default='none')
    # data = models.OneToOneField(RequestData, verbose_name='接口数据', on_delete=models.CASCADE)


class RequestData(ModelBase):
    class Meta:
        verbose_name_plural = verbose_name = '请求数据'
    api = models.ForeignKey(Api, verbose_name='接口', on_delete=models.CASCADE)

    def __str__(self):
        return self.api.name + '-请求数据'

    def run(self, env=None):
        if env:
            pass


class ApiDoc(ModelBase):
    class Meta:
        verbose_name_plural = verbose_name = '接口文档'
    api = models.OneToOneField(Api, verbose_name='接口', on_delete=models.CASCADE)
    markdown = models.TextField('内容', default='')
 
    def __str__(self):
        return self.api.name + '接口文档'


class ParamVariable(ModelWithKey):
    class Meta:
        verbose_name_plural = verbose_name = 'URL参数'

    data = models.ForeignKey(RequestData, verbose_name='请求数据', on_delete=models.CASCADE)
    value = models.CharField('变量值', max_length=200)


class HeaderVariable(ModelWithKey):
    class Meta:
        verbose_name_plural = verbose_name = '请求头'

    data = models.ForeignKey(RequestData, verbose_name='请求数据', on_delete=models.CASCADE)
    value = models.CharField('变量值', max_length=200)


class FormVariable(ModelWithKey):
    class Meta:
        verbose_name_plural = verbose_name = '表单参数'

    data = models.ForeignKey(RequestData, verbose_name='请求数据', on_delete=models.CASCADE)
    value = models.CharField('变量值', max_length=200)


# class JSONVariable(ModelWithKey):
#     class Meta:
#         verbose_name_plural = verbose_name = 'JSON参数'

#     data = models.ForeignKey(RequestData, verbose_name='请求数据', on_delete=models.CASCADE)
#     value = models.CharField('变量值', max_length=200)


class MultipartVariable(ModelWithKey):
    class Meta:
        verbose_name_plural = verbose_name = '复合表单参数'

    data = models.ForeignKey(RequestData, verbose_name='请求数据', on_delete=models.CASCADE)
    value = models.CharField('变量值', max_length=200)


class RawData(ModelWithKey):
    class Meta:
        verbose_name_plural = verbose_name = 'Raw请求数据'

    CONTENT_TYPE_CHOICES = (
        ('text/plain', '纯文本'),
        ('text/html', 'HTML'),
        ('application/xml', 'XML'),
        ('application/json', 'JSON'),

    )
    data = models.OneToOneField(RequestData, verbose_name='请求数据', on_delete=models.CASCADE)
    content_type = models.CharField('内容类型', max_length=100, choices=CONTENT_TYPE_CHOICES, default='text/plain')
    raw = models.TextField('请求数据')


class BinaryData(ModelWithKey):
    class Meta:
        verbose_name_plural = verbose_name = '二进制请求数据'
    data = models.OneToOneField(RequestData, verbose_name='请求数据', on_delete=models.CASCADE)
    file_path = models.FileField('上传文件')
