from django.contrib import admin
from .models import Paciente, Consulta

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'data_nascimento', 'email', 'telefone']
    search_fields = ['nome', 'email']

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ['paciente', 'data', 'motivo', 'estado']
    list_filter = ['estado']
