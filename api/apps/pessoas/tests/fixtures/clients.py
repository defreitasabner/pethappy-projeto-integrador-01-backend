import pytest

@pytest.fixture
def nao_autenticado_client():
    from rest_framework.test import APIClient
    return APIClient()