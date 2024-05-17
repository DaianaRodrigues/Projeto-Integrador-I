"""
URL configuration for Barbearia_Royal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import settings, views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.lista, name='lista'),
    path('index/', views.pagina_prin, name='principal'),
    path('cadastro_sucesso/', views.pagina_sucesso, name='cadastro_sucesso'),
    path('agendamento/', views.agendamento_view, name='agendamento'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('agenda_sucesso/', views.agenda_sucesso, name='agenda_sucesso'),
] + static(settings.STATIC_URL)

