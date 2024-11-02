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
    veterinario = models.TextField(
        Veterinario,
        verbose_name = 'Veterinário',
        related_name = 'pets',
        blank=True,
        null = True,
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
    alimentacao = models.TextField(
        blank=True, 
        null=True
    )
    cuidadoespecial = models.TextField(
        blank=True,
        null=True
    )
    medicamento = models.TextField(
        blank=True, 
        null=True
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
    
class Servico(models.Model):
    STATUSSERVICO_CHOICES = (
        ("Orcado"), ("Aprovado"),("Executado"),("Cancelado")
    )


    datahorasolic=models.DateTimeField()
    valororcado=models.DecimalField(
        max_length=3, 
        decimal_places=2
    )
    valorfaturado=models.DecimalField(
        max_length=3,
        decimal_places=2
    )
    datahorainicio=models.DateTimeField()
    datehorafim=models.DateTimeField()
    statusservico=models.CharField(
        max_length=15,
          blank=False, 
          null=False, 
          choices=STATUSSERVICO_CHOICES
    )
    observacao = models.TextField(
        blank=True,
        null=True
    )
    funcionario=models.ForeignKey(
        Funcionario, 
        on_delete=models.CASCADE
    )
    tiposervico=models.ForeignKey(
        Tiposervico,
        on_delete=models.CASCADE
    )
    pet=models.ManyToManyField(
        Pet, 
        on_delete=models.CASCADE
    )
    turminha=models.ForeignKey(
        Turminha,on_delete=models.CASCADE
    )

    def __str__(self):
        return self.pet.nome     
class Turminha(models.Model):
    datahorainicio=models.DateTimeField()
    datahorafim=models.DateTimeField()
    funcionario=models.ForeignKey(
        Funcionario, 
        on_delete=models.CASCADE
    )
    totalvagas=models.IntegerField()
    vagasocupadas=models.IntegerField()
    tiposervico=models.ForeignKey(
        Tiposervico, 
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.tiposervico.tiposerv

