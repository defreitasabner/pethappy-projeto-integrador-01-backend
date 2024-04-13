from rest_framework import viewsets

from pet_happy.models import Cliente
from pet_happy.serializers import ClienteSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
