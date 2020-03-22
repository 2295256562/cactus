from django.http import JsonResponse
from rest_framework import generics, mixins, viewsets

from api_test import serializers
from api_test import models

class BaseView(mixins.ListModelMixin, mixins.CreateModelMixin,
               mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
               viewsets.GenericViewSet): ...


class Project(BaseView):
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer


class Env(BaseView):
    queryset = models.Env.objects.all()
    serializer_class = serializers.EnvSerializer


class Variable(BaseView):
    queryset = models.Variable.objects.all()
    serializer_class = serializers.VariableSerializer


class Tag(BaseView):
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer


class ApiCategory(BaseView):
    queryset = models.ApiCategory.objects.all()
    serializer_class = serializers.ApiCategorySerializer


class Api(BaseView):
    queryset = models.Api.objects.all()
    serializer_class = serializers.ApiSerializer


class TestCase(BaseView):
    queryset = models.TestCase.objects.all()
    serializer_class = serializers.TestCaseSerializer

    def parse(self, request, *args, **kwargs):
        env_id = request.GET.get('env_id')  # todo check
        case = self.get_object()
        data = dict(name=case.name, description=case.description)
        data['tags'] = [tag.name for tag in case.tags.all()]
        data['steps'] = [step.parse(env_id=env_id) for step in case.steps.all()]
        return JsonResponse(data)

    def run(self,request, *args, **kwargs):
        env_id = request.GET.get('env_id')  # todo check
        case = self.get_object()
        result = case.run(env_id=env_id)
        return JsonResponse(result)

    def copy(self, request, *args, **kwargs):
        case = self.get_object()
        new_case = models.TestCase.objects.create(name=case.name, description=case.description, project=case.project)
        [new_case.tags.add(tag) for tag in case.tags.all()]
        return JsonResponse({'code': 0, 'message': '复制成功'})


class TestStep(BaseView):
    queryset = models.TestStep.objects.all()
    serializer_class = serializers.TestStepSerializer

    def parse(self, request, *args, **kwargs):
        env_id = request.GET.get('env_id')  # todo check
        step = self.get_object()
        data = step.parse(env_id=env_id)
        return JsonResponse(data)

    def run(self,request, *args, **kwargs):
        env_id = request.GET.get('env_id')  # todo check
        step = self.get_object()
        result = step.run(env_id=env_id)
        return JsonResponse(result)

    def copy(self, request, *args, **kwargs):
        step = self.get_object()
        models.TestStep.objects.create(name=step.name, description=step.description, case=step.case,
                                       order=step.order+1, api=step.api, skip=step.skip, request=step.request,
                                       extract=step.extract, check=step.check)
        return JsonResponse({'code': 0, 'message': '复制成功'})


class TestSuite(BaseView):
    queryset = models.TestSuite.objects.all()
    serializer_class = serializers.TestSuiteSerializer

    def parse(self, request, *args, **kwargs):  # todo
        env_id = request.GET.get('env_id')  # todo check
        suite = self.get_object()
        data = dict(name=suite.name, description=suite.description)
        data['tags'] = [tag.name for tag in suite.tags.all()]
        data['steps'] = [step.parse(env_id=env_id) for step in suite.steps.all()]
        return JsonResponse(data)

    def run(self,request, *args, **kwargs):  # todo
        env_id = request.GET.get('env_id')  # todo check
        suite = self.get_object()
        result = suite.run(env_id=env_id)
        return JsonResponse(result)

    def copy(self, request, *args, **kwargs):  # todo
        suite = self.get_object()
        new_suite = models.TestCase.objects.create(name=suite.name, description=suite.description, project=suite.project)
        [new_suite.tags.add(tag) for tag in suite.tags.all()]
        return JsonResponse({'code': 0, 'message': '复制成功'})


    def import_postman(self, request, *args, **kwargs):
        pass


    def export(self, request, * args, **kwargs):
        pass


class TestReport(BaseView):
    queryset = models.TestReport.objects.all()
    serializer_class = serializers.TestReportSerializer
