from django.db import models
from django.contrib.auth.models import User

class Barbeiro(models.Model):
    nome = models.CharField(max_length=100)
    numero_tel = models.CharField(max_length=15)

    def __str__(self):
        return self.nome
    
class Servico(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20, null=True)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=20)

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.nome
    
class Agendamento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    barbeiro = models.ForeignKey(Barbeiro, on_delete=models.CASCADE)
    servico = models.ManyToManyField(Servico)
    data_hora = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Agendamento para {self.cliente} com {self.barbeiro} em {self.data_hora}"
    
class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Adicione quaisquer campos adicionais que deseja ao perfil de usuário
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


