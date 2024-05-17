from django import forms
from .models import Cliente
from django.contrib.auth.forms import UserCreationForm

class CadastroForm(UserCreationForm):
    email = forms.EmailField()

    email = forms.EmailField(label="E-mail")
    nome = forms.CharField(label="Nome")
    telefone = forms.CharField(label="Telefone")
    password1 = forms.CharField(label="Senha")
    password2 = forms.CharField(label="Confirme sua senha")

    class Meta:
        model = Cliente
        fields = ['nome', 'telefone', 'email', 'password1', 'password2']
