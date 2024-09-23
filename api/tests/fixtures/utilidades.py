import pytest
from django.urls import reverse

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