from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

def taskList(request):
    return render(request, 'tasks/list.html')

def agendamento_view(request):
    return render(request, 'tasks/agendamento.html')

def cadastro_view(request):
    return render(request, 'tasks/cadastro.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('agendamento')  # Substitua 'home' pelo nome da sua URL de destino pós-login
        else:
            # Retorne uma mensagem de erro se a autenticação falhar
            return render(request, 'base.html', {'error': 'Nome de usuário ou senha inválidos'})
    return render(request, 'base.html')


