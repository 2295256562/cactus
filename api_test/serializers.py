from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination

from api_test import models


class MyPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page'
    page_size_query_param = 'pageSize'
    max_page_size = 100


class SerilizerBase(serializers.ModelSerializer):
    created = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    modified = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')


class ProjectSerializer(SerilizerBase):
    class Meta:
        model = models.Project
        fields = '__all__'


class EnvSerializer(SerilizerBase):
    class Meta:
        model = models.Env
        fields = '__all__'


class VariableSerializer(SerilizerBase):
    class Meta:
        model = models.Variable
        fields = '__all__'


class TagSerializer(SerilizerBase):
    class Meta:
        model = models.Tag
        fields = '__all__'


class ApiCategorySerializer(SerilizerBase):
    class Meta:
        model = models.ApiCategory
        fields = '__all__'


class ApiSerializer(SerilizerBase):
    class Meta:
        model = models.Api
        fields = '__all__'


class TestCaseSerializer(SerilizerBase):
    class Meta:
        model = models.TestCase
        fields = '__all__'


class TestStepSerializer(SerilizerBase):
    class Meta:
        model = models.TestStep
        fields = '__all__'


class TestSuiteSerializer(SerilizerBase):
    class Meta:
        model = models.TestSuite
        fields = '__all__'


class TestReportSerializer(SerilizerBase):
    class Meta:
        model = models.TestReport
        fields = '__all__'