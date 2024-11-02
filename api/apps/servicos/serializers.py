from rest_framework import serializers
from django.db import transaction

from servicos.models import Servico
from pessoas.models import Funcionario
from pessoas.serializers import FuncionarioSerializer
from pets.models import Pet
from pets.serializers import PetSerializer


class ServicoSerializer(serializers.ModelSerializer):
    funcionario = FuncionarioSerializer(read_only = True)
    pets = PetSerializer(many = True, required = False)
    funcionario_id = serializers.PrimaryKeyRelatedField(queryset = Funcionario.objects.all(), write_only = True)
    pets_ids = serializers.PrimaryKeyRelatedField(queryset = Pet.objects.all(), many =  True, write_only = True)
    class Meta:
        model = Servico
        fields = (
            'id', 'funcionario', 'tipo', 'status', 
            'data_hora_criacao', 'data_hora_inicio', 'data_hora_fim',
            'pets', 'funcionario_id', 'pets_ids',
        )

    @transaction.atomic
    def create(self, validated_data):
        servico = Servico(
            funcionario = validated_data.get('funcionario_id'),
            tipo = validated_data.get('tipo'),
            status = validated_data.get('status'),
            data_hora_inicio = validated_data.get('data_hora_inicio'),
            data_hora_fim = validated_data.get('data_hora_fim'),
        )
        servico.save()
        if validated_data.get('pets_ids'):
            servico.pets.set(validated_data['pets_ids'])
        return servico
    
    @transaction.atomic
    def update(self, instance, validated_data):
        instance.funcionario = validated_data.get('funcionario_id')
        instance.tipo = validated_data.get('tipo')
        instance.status = validated_data.get('status')
        instance.data_hora_inicio = validated_data.get('data_hora_inicio')
        instance.data_hora_fim = validated_data.get('data_hora_fim')
        if validated_data.get('pets_ids'):
            instance.pets.set(validated_data['pets_ids'])
        instance.save()
        return instance

