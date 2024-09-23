import pytest
from django.contrib.auth.models import User

from pessoas.models import Pessoa, Cliente, Endereco, Telefone, Funcionario

@pytest.fixture
def novo_cliente_db(db):
    def criar_novo_cliente(**kwargs):
        pessoa = Pessoa.objects.create(nome = kwargs['pessoa']['nome'])
        endereco = Endereco(pessoa = pessoa, **kwargs['pessoa']['endereco'])
        endereco.save()
        for dados_telefone in kwargs['pessoa']['telefones']:
            telefone = Telefone(pessoa = pessoa, **dados_telefone)
            telefone.save()
        cliente = Cliente.objects.create(pessoa = pessoa)
        return cliente
    return criar_novo_cliente

@pytest.fixture
def novo_funcionario_db(db):
    def criar_novo_funcionario(**kwargs):
        pessoa = Pessoa.objects.create(nome = kwargs['pessoa']['nome'])
        endereco = Endereco(pessoa = pessoa, **kwargs['pessoa']['endereco'])
        endereco.save()
        for dados_telefone in kwargs['pessoa']['telefones']:
            telefone = Telefone(pessoa = pessoa, **dados_telefone)
            telefone.save()
        usuario = User.objects.create_user(
            username = kwargs['usuario']['username'],
            password = kwargs['usuario']['password'],
            email = kwargs['usuario']['email'],
        )
        funcionario = Funcionario.objects.create(pessoa = pessoa, usuario = usuario)
        return funcionario
    return criar_novo_funcionario