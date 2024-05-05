import pytest
from django.urls import reverse

@pytest.fixture
def clientes_url():
    return reverse('pessoas:clientes-create')