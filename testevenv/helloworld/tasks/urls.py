from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.taskList, name='task-list'),
    path('base/', views.pagina_prin, name='principal'),
    path('cadastro_sucesso/', views.pagina_sucesso, name='cadastro_sucesso'),
    path('agendamento/', views.agendamento_view, name='agendamento'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)