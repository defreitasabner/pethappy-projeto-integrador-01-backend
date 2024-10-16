from rest_framework import viewsets

from pessoas.models import Cliente, Funcionario
from pessoas.serializers import ClienteSerializer, UpdateClienteSerializer, FuncionarioSerializer, UpdateFuncionarioSerializer
from pessoas.filters import ClienteFilter, FuncionarioFilter

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    search_fields = ('pessoa__nome',)
    ordering_fields = ('pessoa__nome',)
    ordering = ('pessoa__nome',)
    filterset_class = ClienteFilter

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return UpdateClienteSerializer
        return ClienteSerializer

class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    search_fields = ('pessoa__nome', 'usuario__username')
    ordering_fields = ('pessoa__nome',)
    ordering = ('pessoa__nome',)
    filterset_class = FuncionarioFilter

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return UpdateFuncionarioSerializer
        return FuncionarioSerializer