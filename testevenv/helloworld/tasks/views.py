from django.shortcuts import render
from django.http import HttpResponse


def helloworld(request):
    return HttpResponse('Hello World!')

def taskList(request):
    return render(request, 'tasks/list.html')

def agendamento_view(request):
    return render(request, 'tasks/agendamento.html')

def cadastro_view(request):
    return render(request, 'tasks/cadastro.html')


