import pytest
from django.urls import reverse
from django.contrib.auth.models import User

@pytest.fixture
def obter_url():
    def gerar_url(view_basename, id = None):
        if id:
            return reverse(f'{view_basename}-detail', kwargs = { 'pk': 1 })
        return reverse(f'{view_basename}-list')
    return gerar_url

@pytest.fixture
def nao_autenticado_client():
    from rest_framework.test import APIClient
    return APIClient()

@pytest.fixture
def usuario_padrao_teste():
    User.objects.create_user('teste', 'teste@teste.com', '12345678')