from django.db import models
from pessoas.models import Cliente, Veterinario

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
    ),
    peso_min = models.IntegerField(
        verbose_name = 'Peso Mínimo',
        unique = True,
        null = False,
    ),
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
    veterinario = models.ForeignKey(
        Veterinario,
        verbose_name = 'Veterinário',
        related_name = 'pets',
        on_delete = models.DO_NOTHING,
        null = True,
    )
    nome = models.CharField(
        verbose_name = 'Nome da Categoria',
        max_length = 150,
        null = False,
        blank = False,
    ),
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

    def __str__(self) -> str:
        return self.nome
    
class Medicamento(models.Model):
    pet = models.ForeignKey(
        Pet,
        verbose_name = 'Pet',
        related_name = 'medicamentos',
        on_delete = models.CASCADE,
        null = False,
        blank = False,
    )
    nome = models.CharField(
        verbose_name = 'Nome do Medicamento',
        max_length = 150,
        null = False,
        blank = False, 
    )
    posologia = models.CharField(
        verbose_name = 'Posologia',
        help_text = 'Informações sobre horário, frequência e quantidades das doses.',
        max_length = 300,
        null = False,
        blank = False,
    ),
    observacoes = models.CharField(
        verbose_name = 'Outras Observações', 
        max_length = 300,
        null = False,
        blank = True,
    )

    def __str__(self) -> str:
        return self.nome
    
class Alimento(models.Model):
    pet = models.ForeignKey(
        Pet,
        verbose_name = 'Pet',
        related_name = 'alimentos',
        on_delete = models.CASCADE,
        null = False,
        blank = False,
    )
    descricao = models.CharField(
        verbose_name = 'Descrição do Alimento (Nome)',
        max_length = 150,
        null = False,
        blank = False, 
    )
    quantidade = models.CharField(
        verbose_name = 'Descrição da Quantidade',
        max_length = 150,
        null = False,
        blank = False, 
    )
    periodo = models.CharField(
        verbose_name = 'Período',
        max_length = 100,
        null = False,
        blank = False, 
    )
    local = models.CharField(
        verbose_name = 'Local',
        max_length = 300,
        null = False,
        blank = False,
    )
    observacoes = models.CharField(
        verbose_name = 'Outras Observações',
        max_length = 300,
        null = False,
        blank = True,
    )

    def __str__(self) -> str:
        return f'{self.descricao}: {self.periodo} ({self.local})'
    
class CuidadoEspecial(models.Model):
    pet = models.ForeignKey(
        Pet,
        verbose_name = 'Pet',
        related_name = 'cuidados_especiais',
        on_delete = models.CASCADE,
        null = False,
        blank = False,
    )
    OUTROS = 'O'
    TIPO_CHOICES = [
        (OUTROS, 'Outros'),
        ('D', 'Doença'),
        ('E', 'Emocional'),
    ]
    tipo = models.CharField(
        verbose_name = 'Tipo de Cuidado',
        max_length = 1,
        choices = TIPO_CHOICES,
        default = OUTROS,
        null = False,
    )
    descricao = models.CharField(
        verbose_name = 'Descrição do Cuidado Especial',
        max_length = 300,
        null = False,
        blank = False,
    )

    def __str__(self) -> str:
        return self.tipo
