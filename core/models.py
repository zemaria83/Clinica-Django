from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=200)
    data_nascimento = models.DateField()
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name_plural = 'Pacientes'


class Consulta(models.Model):
    ESTADO_CHOICES = [
        ('agendada', 'Agendada'),
        ('realizada', 'Realizada'),
        ('cancelada', 'Cancelada'),
    ]
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='consultas')
    data = models.DateTimeField()
    motivo = models.CharField(max_length=300)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='agendada')
    notas = models.TextField(blank=True)

    def __str__(self):
        return f"{self.paciente.nome} — {self.data:%d/%m/%Y}"

    class Meta:
        ordering = ['-data']