from rest_framework import viewsets

from pets.models import Categoria, Porte, Pet
from pets.serializers import CategoriaSerializer, PorteSerializer, PetSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class PorteViewSet(viewsets.ModelViewSet):
    queryset = Porte.objects.all()
    serializer_class = PorteSerializer

class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
