from rest_framework import routers

from pessoas.views import ClienteViewSet, FuncionarioViewSet


pessoas_router = routers.DefaultRouter()
pessoas_router.register('clientes', ClienteViewSet, basename = 'Clientes')
pessoas_router.register('funcionarios', FuncionarioViewSet, basename = 'Funcionários')