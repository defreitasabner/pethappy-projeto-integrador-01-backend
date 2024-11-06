from django.db import models

from pessoas.models import Funcionario
from pets.models import Pet


class Servico(models.Model):

    funcionario = models.ForeignKey(
        Funcionario,
        on_delete = models.SET_NULL,
        null = True,
    )

    TIPO_CHOICES = (
        ('H', 'Hospedagem'),
        ('P', 'Passeio'),
        ('V', 'Visita'),
    )
    tipo = models.CharField(
        verbose_name = 'Tipo de Serviço',
        max_length = 1,
        choices = TIPO_CHOICES,
        null = False,
        blank = False,
    )

    AGENDADO = 'A'
    STATUS_CHOICES = (
        ('A', 'Agendado'),
        ('B', 'Em Andamento'),
        ('C', 'Concluído'),
        ('D', 'Cancelado')
    )
    status = models.CharField(
        verbose_name = 'Status do Serviço',
        max_length = 1,
        choices = STATUS_CHOICES,
        default = AGENDADO,
        null = False,
        blank = False,
    )

    data_hora_criacao = models.DateTimeField(auto_now = True)
    
    data_hora_inicio = models.DateTimeField(
        blank = False,
        null = False
    )
    
    data_hora_fim = models.DateField(
        blank = True,
        null = True,
    )
    
    pets = models.ManyToManyField(
        Pet,
        verbose_name = 'Pets',
        related_name = 'servicos',
    )
