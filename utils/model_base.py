from django.db import models
from django.contrib import auth

User = auth.get_user_model()

NULLABLE = dict(null=True, blank=True)
NULLABLE_FK = dict(on_delete=models.CASCADE, null=True, blank=True)


class ModelBase(models.Model):
    class Meta:
        abstract = True

    created = models.DateTimeField('创建时间', auto_now_add=True)
    modified = models.DateTimeField('最后修改时间', auto_now=True)


class ModelWithKey(ModelBase):
    class Meta:
        abstract = True

    key = models.CharField("变量", max_length=200)

    def __str__(self):
        return self.key

class ModelWithName(ModelBase):
    class Meta:
        abstract = True

    name = models.CharField("名称", max_length=200)

    def __str__(self):
        return self.name


class ModelWithDesc(ModelWithName):
    class Meta:
        abstract = True

    description = models.CharField('描述', max_length=500, **NULLABLE)


class ModelWithUser(ModelWithDesc):
    class Meta:
        abstract = True

    creator = models.ForeignKey(User, verbose_name='创建人', on_delete=models.CASCADE)
    edit_user = models.ForeignKey(User, verbose_name='编辑人', on_delete=models.CASCADE)
