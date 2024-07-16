from rest_framework import viewsets
from rest_framework import generics

from pets.models import Categoria, Porte, Pet
from pets.serializers import CategoriaSerializer, PorteSerializer, PetSerializer, ListarPetsDoClienteSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class PorteViewSet(viewsets.ModelViewSet):
    queryset = Porte.objects.all()
    serializer_class = PorteSerializer

class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

class ListarPetsDoClienteView(generics.ListAPIView):
    """Lista todos os pets de um determinado cliente"""
    serializer_class = ListarPetsDoClienteSerializer
    def get_queryset(self):
        queryset = Pet.objects.filter(tutor_id = self.kwargs['pk'])
        return queryset
