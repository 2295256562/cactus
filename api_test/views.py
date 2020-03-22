from rest_framework import generics
from api_test import serializers
from api_test import models


class ProjectList(generics.ListCreateAPIView):
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer


class EnvList(generics.ListCreateAPIView):
    queryset = models.Env.objects.all()
    serializer_class = serializers.EnvSerializer


class EnvDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Env.objects.all()
    serializer_class = serializers.EnvSerializer


class VariableList(generics.ListCreateAPIView):
    queryset = models.Variable.objects.all()
    serializer_class = serializers.VariableSerializer


class VariableDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Variable.objects.all()
    serializer_class = serializers.VariableSerializer


class TagList(generics.ListCreateAPIView):
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer


class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer


class ApiCategoryList(generics.ListCreateAPIView):
    queryset = models.ApiCategory.objects.all()
    serializer_class = serializers.ApiCategorySerializer


class ApiCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ApiCategory.objects.all()
    serializer_class = serializers.ApiCategorySerializer


class ApiList(generics.ListCreateAPIView):
    queryset = models.Api.objects.all()
    serializer_class = serializers.ApiSerializer


class ApiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Api.objects.all()
    serializer_class = serializers.ApiSerializer


class TestCaseList(generics.ListCreateAPIView):
    queryset = models.TestCase.objects.all()
    serializer_class = serializers.TestCaseSerializer


class TestCaseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.TestCase.objects.all()
    serializer_class = serializers.TestCaseSerializer


class TestStepList(generics.ListCreateAPIView):
    queryset = models.TestStep.objects.all()
    serializer_class = serializers.TestStepSerializer


class TestStepDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.TestStep.objects.all()
    serializer_class = serializers.TestStepSerializer


class TestSuiteList(generics.ListCreateAPIView):
    queryset = models.TestSuite.objects.all()
    serializer_class = serializers.TestSuiteSerializer


class TestSuiteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.TestSuite.objects.all()
    serializer_class = serializers.TestSuiteSerializer


class TestReportList(generics.ListCreateAPIView):
    queryset = models.TestReport.objects.all()
    serializer_class = serializers.TestReportSerializer


class TestReportDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.TestReport.objects.all()
    serializer_class = serializers.TestReportSerializer
