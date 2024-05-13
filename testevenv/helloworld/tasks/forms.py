from django import forms
from .models import Cliente

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'telefone', 'email', 'senha']
        widgets = {
            'senha': forms.PasswordInput(),
        }
