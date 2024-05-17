from django.shortcuts import render, redirect
from .forms import CadastroForm
from django.contrib.auth import authenticate, login


def lista(request):
    return render(request, 'list.html')

def pagina_prin(request):
    return render(request, 'Barbearia_Royal/index.html')

def agendamento_view(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            # Aqui você pode adicionar lógica adicional, como criptografar a senha antes de salvar
            form.save()
            return redirect('cadastro_sucesso')
    else:
        form = CadastroForm()  # Fora do bloco de condição POST
    return render(request, 'agendamento.html', {'form': form})

def cadastro_view(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            # Salvando o usuário
            user = form.save()
            # Autenticando o usuário
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('cadastro_sucesso')  # Redirecionar para a página de sucesso após o cadastro
    else:
        form = CadastroForm()
    return render(request, 'cadastro.html', {'form': form})

def pagina_sucesso(request):
    return render(request, 'cadastro_sucesso.html')

def agenda_sucesso(request):
    return render(request, 'agenda_sucesso.html')

def minha_view(request):
    if request.user.is_authenticated:
        username = request.user.username
        # Faça o que quiser com as informações do usuário autenticado
        return render(request, 'agendamento.html', {'username': username})
    else:
        # Redirecione o usuário para a página de login
        return redirect('cadastro')


