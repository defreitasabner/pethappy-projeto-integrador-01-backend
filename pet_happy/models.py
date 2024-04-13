from django.db import models

class Cliente(models.Model):
    nome = models.CharField(
        verbose_name = 'Nome do Cliente',
        max_length = 200,
        null = False,
        blank = False,
    )

    def __str__(self) -> str:
        return self.nome

class Endereco(models.Model):
    cliente = models.OneToOneField(
        Cliente,
        verbose_name = 'Endereço do Cliente',
        related_name = 'endereco',
        on_delete = models.CASCADE,
    )
    cidade = models.CharField(
        verbose_name = 'Nome da Cidade',
        max_length = 100, 
        null = False,
    )
    bairro = models.CharField(
        verbose_name = 'Nome do Bairro',
        max_length = 100,
        null = False,
    )
    rua = models.CharField(
        verbose_name = 'Nome da Rua',
        max_length = 100,
        null = False,
    )
    numero = models.CharField(
        verbose_name = 'Número da Residência',
        max_length = 30,
        null = False,
    )
    complemento = models.CharField(
        verbose_name = 'Informações Complementares',
        max_length = 100,
        null = False,
        blank = True,
    )

    def __str__(self) -> str:
        return f'Rua {self.rua}, {self.numero}'

class Telefone(models.Model):
    cliente = models.ForeignKey(
        Cliente,
        verbose_name = 'Cliente',
        related_name = 'telefones',
        on_delete = models.CASCADE,
        null = False
    )
    numero =  models.CharField(
        verbose_name = 'Número de Telefone',
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