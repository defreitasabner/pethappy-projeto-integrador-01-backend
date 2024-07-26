import pytest
from rest_framework import status

import json

from pessoas.models import Funcionario
from .mocks.funcionario_mock import FuncionarioMock

@pytest.mark.django_db
class TestFuncionario:

    def test_cadastrar_novo_funcionario_com_dados_validos(self, unauthenticated_client):
        response = unauthenticated_client.post(
            'http://localhost:8000/funcionarios/',
            json.dumps(FuncionarioMock.CADASTRAR_DADOS_VALIDOS),
            content_type = 'application/json',
        )
        assert response.status_code == status.HTTP_201_CREATED

    def test_cadastrar_novo_funcionario_com_dados_invalidos(self, unauthenticated_client):
        response = unauthenticated_client.post(
            'http://localhost:8000/funcionarios/',
            json.dumps(FuncionarioMock.CADASTRAR_DADOS_INVALIDOS),
            content_type = 'application/json',
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_atualizar_apenas_email_do_funcionario_com_dados_validos(self, unauthenticated_client):
        response = unauthenticated_client.post(
            'http://localhost:8000/funcionarios/',
            json.dumps(FuncionarioMock.CADASTRAR_DADOS_VALIDOS),
            content_type = 'application/json',
        )
        if response.status_code == status.HTTP_201_CREATED:
            funcionario_id = response.data['id']
            update_response = unauthenticated_client.put(
                f'http://localhost:8000/funcionarios/{funcionario_id}/',
                json.dumps(FuncionarioMock.ATUALIZAR_EMAIL),
                content_type = 'application/json',
            )
            funcionario = Funcionario.objects.all().first()

            assert update_response.status_code == status.HTTP_200_OK
            assert funcionario.usuario.email == FuncionarioMock.ATUALIZAR_EMAIL['usuario']['email']
        else:
            pytest.fail('Falhou ao criar novo funcionário.')