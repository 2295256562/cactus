from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination

from api_test import models


class MyPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page'
    page_size_query_param = 'pageSize'
    max_page_size = 100


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        fields = '__all__'


class EnvSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Env
        fields = '__all__'


class VariableSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Variable
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = '__all__'


class ApiCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ApiCategory
        fields = '__all__'


class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Api
        fields = '__all__'


class TestCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TestCase
        fields = '__all__'


class TestStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TestStep
        fields = '__all__'


class TestSuiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TestSuite
        fields = '__all__'


class TestReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TestReport
        fields = '__all__'