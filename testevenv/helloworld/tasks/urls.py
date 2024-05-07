from django.urls import path
from . import views

urlpatterns = [
    path('', views.taskList, name='task-list'),
    path('', views.agendamento_view, name='agendamento'),
    path('', views.cadastro_view, name='cadastro')
]