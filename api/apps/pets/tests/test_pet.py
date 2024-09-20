import pytest
from rest_framework import status
import json

from pessoas.tests.mocks.cliente_mock import ClienteMock
from .mocks.pet_mock import PetMock

@pytest.mark.django_db
class TestPet:

    def test_cadastrar_novo_pet_com_dados_validos(
        self, 
        unauthenticated_client,
        novo_cliente
    ):
        cliente = novo_cliente(**ClienteMock.CADASTRAR_DADOS_VALIDOS['pessoa'])
        response = unauthenticated_client.post(
            'http://localhost:8000/pets/',
            json.dumps(PetMock.cadastrar_dados_validos(cliente_id = cliente.id)),
            content_type = 'application/json',
        )
        assert response.status_code == status.HTTP_201_CREATED
