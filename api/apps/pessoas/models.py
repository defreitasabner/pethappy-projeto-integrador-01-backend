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
    
    class Meta:
        ordering = ['pessoa__nome',]

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
        return self.pessoa.nome
    
    class Meta:
        ordering = ['pessoa__nome',]

