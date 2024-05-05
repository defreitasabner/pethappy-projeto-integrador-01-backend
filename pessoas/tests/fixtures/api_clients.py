import pytest

@pytest.fixture
def unauthenticated_client():
    from rest_framework.test import APIClient
    return APIClient()