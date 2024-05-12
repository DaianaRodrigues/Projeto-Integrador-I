from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from .models import Usuario

def taskList(request):
    return render(request, 'tasks/list.html')

def pagina_prin(request):
    return render(request, 'base.html')

def agendamento_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Verifica se o usuário existe no banco de dados
        try:
            usuario = Usuario.objects.get(username=username)
            if usuario.password != password:
                messages.error(request, 'Senha incorreta')
                return render(request, 'tasks/list.html')
        except Usuario.DoesNotExist:
            messages.error(request, 'Usuário inválido')
            return render(request, 'tasks/list.html')

        # Se o usuário existe e a senha está correta, faça o que for necessário (como redirecionar para outra página)
        # ...
    return render(request, 'tasks/agendamento.html')

def cadastro_view(request):
    if request.method == 'POST':
        # Capturar os dados do formulário
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        # Criar um novo usuário no banco de dados
        user = User.objects.create_user(username=email, email=email, password=senha)
        user.first_name = nome
        user.save()

        # Redirecionar para a página de sucesso ou outra página desejada
        return redirect('sucesso')

    return render(request, 'tasks/cadastro.html')

def pagina_sucesso(request):
    return render(request, 'tasks/cadastro_sucesso.html')


