import json

import pytest
from django.contrib.auth.models import User
from rest_framework import status

@pytest.mark.django_db
class TestAuthViews:

    def test_obtencao_de_token_bem_sucedida(
        self,
        nao_autenticado_client,
    ):
        dados = { 'username': 'teste', 'password': '12345678' }
        response = nao_autenticado_client.post(
            'http://localhost:8000/token/',
            json.dumps(dados),
            content_type = 'application/json'
        )
        assert response.status_code == status.HTTP_200_OK

    def test_obtencao_de_token_falha(
        self,
        nao_autenticado_client,
    ):
        dados = { 'username': 'naoexiste', 'password': '87654321' }
        response = nao_autenticado_client.post(
            'http://localhost:8000/token/',
            json.dumps(dados),
            content_type = 'application/json'
        )
        assert response.status_code == status.HTTP_401_UNAUTHORIZED