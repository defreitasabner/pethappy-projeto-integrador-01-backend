from django.db import models
from pessoas.models import Cliente

class Categoria(models.Model):
    nome = models.CharField(
        verbose_name = 'Nome',
        max_length = 100,
        null = False,
        blank = False,
    )
    descricao = models.CharField(
        verbose_name = 'Descrição',
        max_length = 300,
        null = False,
    )

    def __str__(self) -> str:
        return self.nome
    
class Porte(models.Model):
    descricao = models.CharField(
        verbose_name = 'Descrição',
        max_length = 100,
        null = False,
        blank = False,
    )
    peso_min = models.IntegerField(
        verbose_name = 'Peso Mínimo',
        unique = True,
        null = False,
    )
    peso_max = models.IntegerField(
        verbose_name = 'Peso Máximo',
        unique = True,
        null = False,
    )

    def __str__(self) -> str:
        return f'{self.descricao}: {self.peso_min} - {self.peso_max}'

class Pet(models.Model):
    
    tutor = models.ForeignKey(
        Cliente,
        verbose_name = 'Tutor do Pet',
        related_name = 'pets',
        on_delete = models.CASCADE,
    )

    nome = models.CharField(
        verbose_name = 'Nome da Categoria',
        max_length = 150,
        null = False,
        blank = False,
    )
    
    data_nascimento = models.DateField(
        verbose_name = 'Data de Nascimento / Adoção',
        null = False,
    )

    INDETERMINADO = 'I'
    SEX_CHOICES = [
        ('F', 'Fêmea'),
        ('M', 'Macho'),
        (INDETERMINADO, 'Indeterminado'),
    ]
    sexo = models.CharField(
        verbose_name = 'Sexo do Pet',
        max_length = 1,
        choices = SEX_CHOICES,
        default = INDETERMINADO,
        null = False,
        blank = False,
    )

    categoria = models.ForeignKey(
        Categoria,
        verbose_name = 'Categoria do Pet',
        related_name = 'pets',
        on_delete = models.PROTECT,
        null = False,
    )

    raca = models.CharField(
        verbose_name = 'Raça do Pet',
        max_length = 100,
        null = False,
        blank = True,
    )

    porte = models.ForeignKey(
        Porte,
        verbose_name = 'Porte do Pet',
        related_name = 'pets',
        on_delete = models.PROTECT,
        null = False,
    )

    alimentos = models.TextField(
        verbose_name = 'Descrição da Alimentação',
        max_length = 1000,
        blank = True, 
        null = True
    )
    
    medicamentos = models.TextField(
        verbose_name = 'Descrição dos medicamentos',
        blank = True, 
        null = True
    )
    
    cuidados_especiais = models.TextField(
        verbose_name = 'Observações',
        blank = True,
        null = True
    )

    veterinario = models.TextField(
        verbose_name = 'Veterinário',
        blank = True,
        null = True,
    )

    def __str__(self) -> str:
        return self.nome

