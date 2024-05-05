import pytest

from pessoas.models import Pessoa, Cliente, Endereco, Telefone

@pytest.fixture
def novo_cliente(db):
    def criar_novo_cliente(**kwargs):
        pessoa = Pessoa.objects.create(nome = kwargs['nome'])
        endereco = Endereco(pessoa = pessoa, **kwargs['endereco'])
        endereco.save()
        for dados_telefone in kwargs['telefones']:
            telefone = Telefone(pessoa = pessoa, **dados_telefone)
            telefone.save()
        cliente = Cliente.objects.create(pessoa = pessoa)
        return cliente
    return criar_novo_cliente