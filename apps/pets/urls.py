from rest_framework import routers

from pets.views import *

pets_router = routers.DefaultRouter()
pets_router.register('categorias', CategoriaViewSet, basename = 'Categorias')
pets_router.register('portes', PorteViewSet, basename = 'Portes')
pets_router.register('pets', PetViewSet, basename = 'Pets')