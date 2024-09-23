from rest_framework import routers

from pets.views import *

pets_router = routers.DefaultRouter()
pets_router.register('categorias', CategoriaViewSet, basename = 'categorias')
pets_router.register('portes', PorteViewSet, basename = 'portes')
pets_router.register('pets', PetViewSet, basename = 'pets')