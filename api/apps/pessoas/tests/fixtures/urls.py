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
def clientes_url():
    def gerar_url(id = None):
        if id:
            return reverse('clientes-detail', kwargs = { 'pk': 1 })
        return reverse('clientes-list')
    return gerar_url

@pytest.fixture
def pets_url():
    def gerar_url(id = None):
        if id:
            return reverse('pets-detail', kwargs = { 'pk': 1 })
        return reverse('pets-list')
    return gerar_url