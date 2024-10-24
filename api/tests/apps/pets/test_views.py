import pytest
from rest_framework import status
import json

from tests.mocks.cliente_mock import ClienteMock
from tests.mocks.pet_mock import PetMock

@pytest.mark.django_db
class TestPetView:

    def test_cadastrar_novo_pet_com_dados_validos(
        self,
        obter_url,
        autenticado_client,
        novo_cliente_db
    ):
        cliente = novo_cliente_db(**ClienteMock.CADASTRAR_DADOS_VALIDOS)
        response = autenticado_client.post(
            obter_url('pets'),
            json.dumps(PetMock.cadastrar_minimo_dados_necessarios(cliente_id = cliente.id)),
            content_type = 'application/json',
        )
        assert response.status_code == status.HTTP_201_CREATED
