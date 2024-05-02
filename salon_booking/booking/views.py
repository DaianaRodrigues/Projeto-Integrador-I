from django.shortcuts import render
from .models import Service

def listaDeServico(request):
    services = Service.objects.all()
    return render(request, 'booking/ListaDeServico.html', {'services': services})

def apontamento(request):
    if request.method == 'POST':
        # Processar o formulário de agendamento aqui
        pass
    else:
        services = Service.objects.all()
        return render(request, 'booking/Apontamento.html', {'services': services})

