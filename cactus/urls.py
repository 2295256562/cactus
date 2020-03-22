from django.contrib import admin
from django.urls import path, include

from api_test import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/api_test/', include('api_test.urls', namespace='api_test')),  # 增加该行
]
