from rest_framework import routers

from pet_happy.views import ClienteViewSet


pet_happy_router = routers.DefaultRouter()
pet_happy_router.register('clientes', ClienteViewSet, basename = 'Clientes')