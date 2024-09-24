import pytest
from rest_framework import status

import json

from pessoas.models import Cliente, Funcionario
from tests.mocks.cliente_mock import ClienteMock
from tests.mocks.funcionario_mock import FuncionarioMock

@pytest.mark.django_db
class TestClienteView:

    def test_cadastrar_novo_cliente_com_dados_validos(
        self,
        obter_url, 
        autenticado_client
    ):
        response = autenticado_client.post(
            obter_url('clientes'),
            json.dumps(ClienteMock.CADASTRAR_DADOS_VALIDOS),
            content_type = 'application/json',
        )
        assert response.status_code == status.HTTP_201_CREATED

    def test_cadastrar_novo_cliente_com_dados_invalidos(
        self,
        obter_url,
        autenticado_client
    ):
        response = autenticado_client.post(
            obter_url('clientes'),
            json.dumps(ClienteMock.CADASTRAR_DADOS_INVALIDOS),
            content_type = 'application/json',
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_atualizar_apenas_endereco_do_cliente_com_dados_validos(
        self,
        obter_url,
        novo_cliente_db, 
        autenticado_client
    ):
        cliente = novo_cliente_db(**ClienteMock.CADASTRAR_DADOS_VALIDOS)
        response = autenticado_client.put(
            obter_url('clientes', cliente.id),
            json.dumps(ClienteMock.ATUALIZAR_ENDERECO),
            content_type = 'application/json',
        )
        cliente_atualizado = Cliente.objects.all().first()

        assert response.status_code == status.HTTP_200_OK
        assert cliente_atualizado.pessoa.endereco.cidade == ClienteMock.ATUALIZAR_ENDERECO['pessoa']['endereco']['cidade']
        assert cliente_atualizado.pessoa.endereco.bairro == ClienteMock.ATUALIZAR_ENDERECO['pessoa']['endereco']['bairro']
        assert cliente_atualizado.pessoa.endereco.rua == ClienteMock.ATUALIZAR_ENDERECO['pessoa']['endereco']['rua']
        assert cliente_atualizado.pessoa.endereco.numero == ClienteMock.ATUALIZAR_ENDERECO['pessoa']['endereco']['numero']
        assert cliente_atualizado.pessoa.endereco.complemento == ClienteMock.ATUALIZAR_ENDERECO['pessoa']['endereco']['complemento']

@pytest.mark.django_db
class TestFuncionarioView:

    def test_cadastrar_novo_funcionario_com_dados_validos(
        self,
        obter_url, 
        autenticado_client
    ):
        response = autenticado_client.post(
            obter_url('funcionarios'),
            json.dumps(FuncionarioMock.CADASTRAR_DADOS_VALIDOS),
            content_type = 'application/json',
        )
        assert response.status_code == status.HTTP_201_CREATED

    def test_cadastrar_novo_funcionario_com_dados_invalidos(
        self,
        obter_url, 
        autenticado_client
    ):
        response = autenticado_client.post(
            obter_url('funcionarios'),
            json.dumps(FuncionarioMock.CADASTRAR_DADOS_INVALIDOS),
            content_type = 'application/json',
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_atualizar_apenas_email_do_funcionario_com_dados_validos(
        self,
        obter_url,
        novo_funcionario_db,
        autenticado_client
    ):
        funcionario = novo_funcionario_db(**FuncionarioMock.CADASTRAR_DADOS_VALIDOS)
        update_response = autenticado_client.put(
            obter_url('funcionarios', funcionario.id),
            json.dumps(FuncionarioMock.ATUALIZAR_EMAIL),
            content_type = 'application/json',
        )
        funcionario = Funcionario.objects.all().first()

        assert update_response.status_code == status.HTTP_200_OK
        assert funcionario.usuario.email == FuncionarioMock.ATUALIZAR_EMAIL['usuario']['email']