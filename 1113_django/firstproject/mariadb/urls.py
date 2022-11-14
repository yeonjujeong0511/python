from django.urls import path
from . import views

urlpatterns = [
    path('mariadbdata/', views.getTestDatas, name="mariadbdata"),
]
