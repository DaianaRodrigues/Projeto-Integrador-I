from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def taskList(request):
    return render(request, 'tasks/list.html')

def pagina_prin(request):
    return render(request, 'base.html')

def agendamento_view(request):
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
            messages.error(request, 'Nome de usuário ou senha inválidos')
            return render(request, 'base.html')
    return render(request, 'base.html')

##def cadastro_view(request):
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

    return render(request, 'cadastro.html')


