from rest_framework import routers

from pet_happy.views import ClienteViewSet, FuncionarioViewSet


pet_happy_router = routers.DefaultRouter()
pet_happy_router.register('clientes', ClienteViewSet, basename = 'Clientes')
pet_happy_router.register('funcionarios', FuncionarioViewSet, basename = 'Funcionários')