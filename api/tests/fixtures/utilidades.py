import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User

@pytest.fixture
def obter_url():
    def gerar_url(view_basename, id = None):
        if id:
            return reverse(f'{view_basename}-detail', kwargs = { 'pk': 1 })
        return reverse(f'{view_basename}-list')
    return gerar_url

@pytest.fixture(scope = 'session')
def nao_autenticado_client():
    return APIClient()

@pytest.fixture(scope = 'session')
def autenticado_client(django_db_blocker):
    with django_db_blocker.unblock():
        client = APIClient()
        usuario = User.objects.first()
        token = RefreshToken.for_user(usuario)
        client.credentials(HTTP_AUTHORIZATION = f'Bearer {str(token.access_token)}')
        return client