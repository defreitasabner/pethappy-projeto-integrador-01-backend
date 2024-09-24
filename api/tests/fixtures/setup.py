import pytest
from django.contrib.auth.models import User

@pytest.fixture(scope = 'session', autouse = True)
def popular_banco_de_dados(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        User.objects.create_user('teste', 'teste@teste.com', '12345678')