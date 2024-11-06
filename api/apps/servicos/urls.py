from rest_framework import routers

from servicos.views import ServicoViewSet


servicos_router = routers.DefaultRouter()
servicos_router.register('servicos', ServicoViewSet, basename = 'servicos')