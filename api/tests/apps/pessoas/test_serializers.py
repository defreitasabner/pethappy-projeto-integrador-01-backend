import pytest

from pessoas.serializers import (
    PessoaSerializer, EnderecoSerializer, TelefoneSerializer, 
    ClienteSerializer, FuncionarioSerializer
)
from pessoas.models import Pessoa, Endereco, Telefone, Cliente
from tests.mocks.cliente_mock import ClienteMock
from tests.mocks.funcionario_mock import FuncionarioMock

@pytest.mark.teste_unidade
class TestPessoaSerializer:

    def test_validacao_pessoa_nome_vazio(self):
        dados_invalidos = {
            "nome": "",
            "endereco": {
                "cidade": "Rio de Janeiro",
                "bairro": "Tijuca",
                "rua": "Delgado de Carvalho",
                "numero": "84",
                "complemento": "Na esquina com a rua Barão de Itapagipe"
            },    
            "telefones": [
                {
                    "numero": "11234567890",
                    "is_contato_emergencia": True
                }
            ]
        }
        pessoa_serializer = PessoaSerializer(data = dados_invalidos)
        assert pessoa_serializer.is_valid() == False

    def test_validacao_pessoa_endereco_campos_vazios(self):
        dados_invalidos = {
            "nome": "Shrek",
            "endereco": {
                "cidade": "Reino Encantado",
                "bairro": "Meu Pãntano",
                "rua": "",
                "numero": "",
                "complemento": ""
            },    
            "telefones": [
                {
                    "numero": "11234567890",
                    "is_contato_emergencia": True
                }
            ]
        }
        pessoa_serializer = PessoaSerializer(data = dados_invalidos)
        assert pessoa_serializer.is_valid() == False


@pytest.mark.teste_unidade
class TestEnderecoSerializer:

    def test_validacao_endereco_valida(self):
        dados_invalidos =  {
            "cidade": "Rio de Janeiro",
            "bairro": "Cinelândia",
            "rua": "Rua do Passeio",
            "numero": "123",
            "complemento": ""
        }
        endereco_serializer = EnderecoSerializer(data = dados_invalidos)
        assert endereco_serializer.is_valid() == True

    def test_validacao_endereco_nao_valida(self):
        dados_invalidos =  {
            "cidade": "",
            "bairro": "",
            "rua": "",
            "numero": "",
            "complemento": ""
        }
        endereco_serializer = EnderecoSerializer(data = dados_invalidos)
        assert endereco_serializer.is_valid() == False


@pytest.mark.teste_unidade
class TestTelefoneSerializer:

    def test_validacao_telefone_valida(self):
        dados_invalidos = {
            'numero': '11234567890',
            'is_contato_emergencia': True
        }
        telefone_serializer = TelefoneSerializer(data = dados_invalidos)
        assert telefone_serializer.is_valid() == True

    def test_validacao_telefone_nao_valida(self):
        dados_invalidos = {
            'numero': '',
            'is_contato_emergencia': True
        }
        telefone_serializer = TelefoneSerializer(data = dados_invalidos)
        assert telefone_serializer.is_valid() == False


@pytest.mark.teste_unidade
class TestClienteSerializer:

    def test_validacao_cliente_valida(self):
        cliente_serializer = ClienteSerializer(data = ClienteMock.CADASTRAR_DADOS_VALIDOS)
        assert cliente_serializer.is_valid() == True

    def test_validacao_cliente_nao_valida(self):
        cliente_serializer = ClienteSerializer(data = ClienteMock.CADASTRAR_DADOS_INVALIDOS)
        assert cliente_serializer.is_valid() == False

    @pytest.mark.django_db
    def test_campos_exposto_cliente(self, novo_cliente_db):
        cliente = novo_cliente_db(**ClienteMock.CADASTRAR_DADOS_VALIDOS)
        cliente_serializer = ClienteSerializer(instance = cliente)
        assert list(cliente_serializer.data.keys()) == ['id', 'pessoa']


@pytest.mark.django_db
class TestFuncionarioSerializer:

    def test_validacao_funcionario_valida(self):
        funcionario_serializer = FuncionarioSerializer(data = FuncionarioMock.CADASTRAR_DADOS_VALIDOS)
        assert funcionario_serializer.is_valid() == True

    def test_validacao_funcionario_nao_valida(self):
        funcionario_serializer = FuncionarioSerializer(data = FuncionarioMock.CADASTRAR_DADOS_INVALIDOS)
        assert funcionario_serializer.is_valid() == False

    def test_campos_exposto_funcionario(self, novo_funcionario_db):
        funcionario = novo_funcionario_db(**FuncionarioMock.CADASTRAR_DADOS_VALIDOS)
        funcionario_serializer = FuncionarioSerializer(instance = funcionario)
        assert set(funcionario_serializer.data.keys()) == set(['id', 'pessoa', 'usuario'])
        assert 'password' not in funcionario_serializer.data['usuario'].keys()
    