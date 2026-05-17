from django.shortcuts import render, get_object_or_404
from .models import Paciente, Consulta

def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'core/lista_pacientes.html', {'pacientes': pacientes})

def detalhe_paciente(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    consultas = paciente.consultas.all()
    return render(request, 'core/detalhe_paciente.html', {
        'paciente': paciente,
        'consultas': consultas,
    })

def lista_consultas(request):
    consultas = Consulta.objects.select_related('paciente').all()
    return render(request, 'core/lista_consultas.html', {'consultas': consultas})