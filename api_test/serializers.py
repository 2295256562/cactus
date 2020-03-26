
from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination
from djcelery.models import PeriodicTask

from api_test import models


class MyPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page'
    page_size_query_param = 'pageSize'
    max_page_size = 100


class SerializerBase(serializers.ModelSerializer):
    created = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', allow_null=True)
    modified = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', allow_null=True)


class ProjectSerializer(SerializerBase):
    class Meta:
        model = models.Project
        fields = '__all__'


class EnvSerializer(SerializerBase):
    class Meta:
        model = models.Env
        fields = '__all__'


class VariableSerializer(SerializerBase):
    class Meta:
        model = models.Variable
        fields = '__all__'


class TagSerializer(SerializerBase):
    class Meta:
        model = models.Tag
        fields = '__all__'


class ApiCategorySerializer(SerializerBase):
    class Meta:
        model = models.ApiCategory
        fields = '__all__'


class ApiSerializer(SerializerBase):
    class Meta:
        model = models.Api
        fields = '__all__'


class TestCaseSerializer(SerializerBase):
    class Meta:
        model = models.TestCase
        fields = '__all__'


class TestStepSerializer(SerializerBase):
    class Meta:
        model = models.TestStep
        fields = '__all__'


class TestSuiteSerializer(SerializerBase):
    class Meta:
        model = models.TestSuite
        fields = '__all__'


class TestReportSerializer(SerializerBase):
    class Meta:
        model = models.TestReport
        fields = '__all__'

class PeriodicTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodicTask
        fields = '__all__'