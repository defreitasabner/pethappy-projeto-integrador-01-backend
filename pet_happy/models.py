from django.db import models
from django.contrib.auth.models import User 
from django.db import transaction

class Pessoa(models.Model):
    nome = models.CharField(
        verbose_name = 'Nome',
        max_length = 150,
        null = False,
        blank = False,
    )

    def __str__(self) -> str:
        return self.nome

class Endereco(models.Model):
    pessoa = models.OneToOneField(
        Pessoa,
        verbose_name = 'Endereço',
        related_name = 'endereco',
        on_delete = models.CASCADE,
    )
    cidade = models.CharField(
        verbose_name = 'Cidade',
        max_length = 100, 
        null = False,
    )
    bairro = models.CharField(
        verbose_name = 'Bairro',
        max_length = 100,
        null = False,
    )
    rua = models.CharField(
        verbose_name = 'Rua',
        max_length = 100,
        null = False,
    )
    numero = models.CharField(
        verbose_name = 'Residência',
        max_length = 30,
        null = False,
    )
    complemento = models.CharField(
        verbose_name = 'Complemento',
        max_length = 100,
        null = False,
        blank = True,
    )

    def __str__(self) -> str:
        return f'Rua {self.rua}, {self.numero}'

class Telefone(models.Model):
    pessoa = models.ForeignKey(
        Pessoa,
        verbose_name = 'Pessoa',
        related_name = 'telefones',
        on_delete = models.CASCADE,
        null = False
    )
    numero =  models.CharField(
        verbose_name = 'Número',
        max_length = 15,
        null = False,
        blank = False,
    )
    is_contato_emergencia = models.BooleanField(
        verbose_name = 'Contato de Emergência',
        null = False,
        default = False,
    )

    def __str__(self) -> str:
        return self.numero

class Cliente(models.Model):
    pessoa = models.OneToOneField(
        Pessoa,
        verbose_name = 'Pessoa',
        related_name = 'cliente',
        on_delete = models.CASCADE,
    )

    @transaction.atomic
    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        if self.pessoa:
            self.pessoa.delete()

class Funcionario(models.Model):
    usuario = models.OneToOneField(
        User,
        verbose_name = 'Usuário',
        related_name = 'funcionario',
        on_delete = models.CASCADE,
    )
    pessoa = models.OneToOneField(
        Pessoa,
        verbose_name = 'Pessoa',
        related_name = 'funcionario',
        on_delete = models.CASCADE,
    )

    @transaction.atomic
    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.pessoa.delete()
        self.usuario.delete()
    
    def __str__(self) -> str:
        return self.nome

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

#TODO: Estudar a real necessidade de ser ter um novo modelo, talvez usar Pessoa diretamente
class Veterinario(models.Model):
    pessoa = models.OneToOneField(
        Pessoa,
        verbose_name = 'Pessoa',
        related_name = 'veterinario',
        on_delete = models.CASCADE,
    )
    clinica = models.CharField(
        verbose_name = 'Nome da Clínica',
        max_length = 150,
        null = False,
        blank = False
    )

    def __str__(self) -> str:
        return self.pessoa

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
        on_delete = models.CASCADE,
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
        null = False,
        blank = False,
        choices = SEX_CHOICES,
        default = INDETERMINADO
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
    OUTROS = 'O'
    TIPO_CHOICES = [
        (OUTROS, 'Outros'),
        ('D', 'Doença'),
        ('E', 'Emocional'),
    ]
    tipo = models.CharField(
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