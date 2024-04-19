from rest_framework import viewsets

from pet_happy.models import Cliente, Funcionario
from pet_happy.serializers import ClienteSerializer, UpdateClienteSerializer, FuncionarioSerializer, UpdateFuncionarioSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return UpdateClienteSerializer
        return ClienteSerializer

class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return UpdateFuncionarioSerializer
        return FuncionarioSerializer