from django.urls import path
from . import views

urlpatterns = [
    path('helloworld/', views.helloworld),
    path('', views.taskList, name='task-list'),
]