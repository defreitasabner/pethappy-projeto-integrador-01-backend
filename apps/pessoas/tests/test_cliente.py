import pytest
from rest_framework import status

import json

from pessoas.models import Cliente
from .mocks.cliente_mock import ClienteMock

@pytest.mark.django_db
class TestCliente:

    def test_cadastrar_novo_cliente_com_dados_validos(self, unauthenticated_client):
        response = unauthenticated_client.post(
            'http://localhost:8000/clientes/',
            json.dumps(ClienteMock.CADASTRAR_DADOS_VALIDOS),
            content_type = 'application/json',
        )
        assert response.status_code == status.HTTP_201_CREATED

    def test_cadastrar_novo_cliente_com_dados_invalidos(self, unauthenticated_client):
        response = unauthenticated_client.post(
            'http://localhost:8000/clientes/',
            json.dumps(ClienteMock.CADASTRAR_DADOS_INVALIDOS),
            content_type = 'application/json',
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_atualizar_apenas_endereco_do_cliente_com_dados_validos(self, unauthenticated_client):
        response = unauthenticated_client.post(
            'http://localhost:8000/clientes/',
            json.dumps(ClienteMock.CADASTRAR_DADOS_VALIDOS),
            content_type = 'application/json',
        )
        if response.status_code == status.HTTP_201_CREATED:
            cliente_id = response.data['id']
            update_response = unauthenticated_client.put(
                f'http://localhost:8000/clientes/{cliente_id}/',
                json.dumps(ClienteMock.ATUALIZAR_ENDERECO),
                content_type = 'application/json',
            )
            cliente = Cliente.objects.all().first()

            assert update_response.status_code == status.HTTP_200_OK
            assert cliente.pessoa.endereco.cidade == ClienteMock.ATUALIZAR_ENDERECO['pessoa']['endereco']['cidade']
            assert cliente.pessoa.endereco.bairro == ClienteMock.ATUALIZAR_ENDERECO['pessoa']['endereco']['bairro']
            assert cliente.pessoa.endereco.rua == ClienteMock.ATUALIZAR_ENDERECO['pessoa']['endereco']['rua']
            assert cliente.pessoa.endereco.numero == ClienteMock.ATUALIZAR_ENDERECO['pessoa']['endereco']['numero']
            assert cliente.pessoa.endereco.complemento == ClienteMock.ATUALIZAR_ENDERECO['pessoa']['endereco']['complemento']
        else:
            pytest.fail('Falhou ao criar novo cliente.')