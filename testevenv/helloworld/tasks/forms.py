from django import forms
from .models import Cliente
from django.contrib.auth.forms import UserCreationForm

class CadastroForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Cliente
        fields = ['nome', 'telefone', 'email', 'password1', 'password2']
