from django_filters import rest_framework as filters 

from pessoas.models import Cliente, Funcionario

class ClienteFilter(filters.FilterSet):
    nome = filters.CharFilter(field_name = 'pessoa__nome', lookup_expr = 'icontains')
    telefone = filters.CharFilter(field_name = 'pessoa__telefones__numero', lookup_expr = 'icontains')
    bairro = filters.CharFilter(field_name = 'endereco__bairro', lookup_expr = 'icontains')
    rua = filters.CharFilter(field_name = 'endereco__rua', lookup_expr = 'icontains')
    class Meta:
        model = Cliente
        fields = ('pessoa',)

class FuncionarioFilter(ClienteFilter):
    username = filters.CharFilter(field_name = 'usuario__username', lookup_expr = 'icontains')
    class Meta:
        model = Funcionario
        fields = ('pessoa',)