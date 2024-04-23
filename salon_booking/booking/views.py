from django.shortcuts import render
from .models import Service

def service_list(request):
    services = Service.objects.all()
    return render(request, 'booking/ListaDeServico.html', {'services': services})

def appointment_create(request):
    if request.method == 'POST':
        # Processar o formulário de agendamento aqui
        pass
    else:
        services = Service.objects.all()
        return render(request, 'booking/Apontamento.html', {'services': services})

