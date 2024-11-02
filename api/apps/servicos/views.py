from rest_framework import viewsets

from servicos.models import Servico
from servicos.serializers import ServicoSerializer

class ServicoViewSet(viewsets.ModelViewSet):
    serializer_class = ServicoSerializer
    queryset = Servico.objects.all()
    search_field = ('funcionario__pessoa__nome',)
    ordering_fields = ('data_hora_inicio',)
    ordering = ('data_hora_inicio',)
