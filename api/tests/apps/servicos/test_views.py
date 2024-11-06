import json
import pytest
from rest_framework import status

from tests.mocks.funcionario_mock import FuncionarioMock
from tests.mocks.cliente_mock import ClienteMock
from tests.mocks.pet_mock import PetMock


@pytest.mark.django_db
class TestServicosView:

    def test_cadastrar_novo_servico(
        self, 
        obter_url,
        autenticado_client,
        novo_cliente_db,
        novo_funcionario_db,
    ):
        funcionario = novo_funcionario_db(**FuncionarioMock.CADASTRAR_DADOS_VALIDOS)
        cliente = novo_cliente_db(**ClienteMock.CADASTRAR_DADOS_VALIDOS)
        pet_response = autenticado_client.post(
            obter_url('pets'),
            json.dumps(PetMock.cadastrar_minimo_dados_necessarios(cliente_id = cliente.id)),
            content_type = 'application/json',
        )
        
        if(pet_response.status_code != status.HTTP_201_CREATED):
            pytest.fail('Falhou ao criar um pet ...')
        
        response = autenticado_client.post(
            obter_url('servicos'),
            json.dumps({
                'funcionario_id': funcionario.id,
                'tipo': 'P',
                'status': 'A',
                'pets_ids': [1],
                'data_hora_inicio': '2020-04-23T00:00:00',
            }),
            content_type = 'application/json',
        )
        
        assert response.status_code == status.HTTP_201_CREATED