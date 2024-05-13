from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UsuarioForm

def lista(request):
    return render(request, 'tasks/list.html')

def pagina_prin(request):
    return render(request, 'base.html')

def agendamento_view(request):
     if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            # Aqui você pode adicionar lógica adicional, como criptografar a senha antes de salvar
            form.save()
            return redirect('cadastro_sucesso')
        else:
            form = UsuarioForm()
        return render(request, 'tasks/agendamento.html', {'form': form})

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

def agenda_sucesso(request):
    return render(request, 'tasks/agenda_sucesso.html')

def minha_view(request):
    if request.user.is_authenticated:
        username = request.user.username
        # Faça o que quiser com as informações do usuário autenticado
        return render(request, 'agendamento.html', {'username': username})
    else:
        # Redirecione o usuário para a página de login
        return redirect('cadastro')


