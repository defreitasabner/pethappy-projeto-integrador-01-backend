import pytest
from rest_framework import status
import json

from pessoas.tests.mocks.cliente_mock import ClienteMock
from .mocks.pet_mock import PetMock

@pytest.mark.django_db
class TestPetView:

    def test_cadastrar_novo_pet_com_dados_validos(
        self,
        pets_url,
        nao_autenticado_client,
        novo_cliente_db
    ):
        cliente = novo_cliente_db(**ClienteMock.CADASTRAR_DADOS_VALIDOS)
        response = nao_autenticado_client.post(
            pets_url(),
            json.dumps(PetMock.cadastrar_dados_validos(cliente_id = cliente.id)),
            content_type = 'application/json',
        )
        assert response.status_code == status.HTTP_201_CREATED
