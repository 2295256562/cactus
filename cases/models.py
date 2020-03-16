from django.db import models
from utils.model_base import ModelBase, ModelWithKey, ModelWithDesc, ModelWithUser, NULLABLE, NULLABLE_FK

from projects.models import Project
from apis.models import Api, RequestData


class TestSuite(ModelWithDesc):
    class Meta:
        verbose_name_plural = verbose_name = '测试套件'
    project = models.ForeignKey(Project, verbose_name='项目', on_delete=models.CASCADE)


class TestCase(ModelWithDesc):
    class Meta:
        verbose_name_plural = verbose_name = '测试用例'

    suite = models.ForeignKey(TestSuite, verbose_name='测试套件', on_delete=models.CASCADE)


class TestStep(ModelWithDesc):
    class Meta:
        verbose_name_plural = verbose_name = '测试步骤'
    case = models.ForeignKey(TestCase, verbose_name='测试用例', on_delete=models.CASCADE)
    # api = models.ForeignKey(Api, verbose_name='接口', on_delete=models.CASCADE)
    data = models.OneToOneField(RequestData, verbose_name='请求数据', on_delete=models.CASCADE)


# class ParamVariable(ModelWithKey):
#     class Meta:
#         verbose_name_plural = verbose_name = 'URL参数'

#     step = models.ForeignKey(TestStep, verbose_name='测试步骤', on_delete=models.CASCADE)
#     value = models.CharField('变量值', max_length=200)



# class HeaderVariable(ModelWithKey):
#     class Meta:
#         verbose_name_plural = verbose_name = '请求头'

#     step = models.ForeignKey(TestStep, verbose_name='测试步骤', on_delete=models.CASCADE)
#     value = models.CharField('变量值', max_length=200)


# class FormVariable(ModelWithKey):
#     class Meta:
#         verbose_name_plural = verbose_name = '表单参数'

#     step = models.ForeignKey(TestStep, verbose_name='测试步骤', on_delete=models.CASCADE)
#     value = models.CharField('变量值', max_length=200)


# class JSONVariable(ModelWithKey):
#     class Meta:
#         verbose_name_plural = verbose_name = 'JSON参数'

#     step = models.ForeignKey(TestStep, verbose_name='测试步骤', on_delete=models.CASCADE)
#     value = models.CharField('变量值', max_length=200)


# class MultipartVariable(ModelWithKey):
#     class Meta:
#         verbose_name_plural = verbose_name = '复合表单参数'

#     step = models.ForeignKey(TestStep, verbose_name='测试步骤', on_delete=models.CASCADE)
#     value = models.CharField('变量值', max_length=200)


# class RawData(ModelWithKey):
#     class Meta:
#         verbose_name_plural = verbose_name = 'Raw请求数据'

#     CONTENT_TYPE_CHOICES = (
#         ('text/plain', '纯文本'),
#         ('text/html', 'HTML'),
#         ('application/xml', 'XML'),
#         ('application/json', 'JSON'),

#     )
#     step = models.OneToOneField(TestStep, verbose_name='测试步骤', on_delete=models.CASCADE)
#     content_type = models.CharField('内容类型', max_length=100, choices=CONTENT_TYPE_CHOICES, default='text/plain')
#     data = models.TextField('请求数据')


# class BinaryData(ModelWithKey):
#     class Meta:
#         verbose_name_plural = verbose_name = '复合表单参数'
#     step = models.OneToOneField(TestStep, verbose_name='测试步骤', on_delete=models.CASCADE)
#     file_path = models.FilePathField('上传文件')
