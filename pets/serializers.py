from rest_framework import serializers
from django.db import transaction

from pets.models import *
from pessoas.serializers import ClienteSerializer, VeterinarioSerializer

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class PorteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Porte
        fields = '__all__'

class MedicamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicamento
        fields = ('id', 'nome', 'posologia', 'observacoes')

class AlimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alimento
        fields = ('id', 'descricao', 'quantidade', 'periodo', 'local', 'observacoes')

class CuidadoEspecialSerializer(serializers.ModelSerializer):
    class Meta:
        model = CuidadoEspecial
        fields = ('id', 'tipo', 'descricao')

class PetSerializer(serializers.ModelSerializer):
    tutor = ClienteSerializer(read_only = True)
    categoria = CategoriaSerializer(read_only = True)
    porte = PorteSerializer(read_only = True)
    medicamentos = MedicamentoSerializer(many = True, required = False)
    alimentos = AlimentoSerializer(many = True, required = False)
    cuidados_especiais = CuidadoEspecialSerializer(many = True, required = False)
    tutor_id = serializers.PrimaryKeyRelatedField(queryset = Cliente.objects.all(), write_only = True)
    categoria_id = serializers.PrimaryKeyRelatedField(queryset = Categoria.objects.all(), write_only = True)
    porte_id = serializers.PrimaryKeyRelatedField(queryset = Porte.objects.all(), write_only = True)
    veterinario = VeterinarioSerializer(required = False)
    class Meta:
        model = Pet
        fields = (
            'id', 'tutor', 'veterinario', 'nome', 
            'data_nascimento', 'sexo', 
            'raca', 'categoria', 'porte',
            'medicamentos', 'alimentos', 'cuidados_especiais',
            'tutor_id', 'categoria_id', 'porte_id'
        )

    @transaction.atomic
    def create(self, validated_data):
        veterinario = None
        if validated_data.get('veterinario'):
            veterinario = VeterinarioSerializer().create(validated_data = validated_data['veterinario'])
        pet = Pet(
            tutor = validated_data['tutor_id'],
            veterinario = veterinario,
            categoria = validated_data['categoria_id'],
            porte = validated_data['porte_id'],
            nome = validated_data['nome'],
            data_nascimento = validated_data['data_nascimento'],
            sexo = validated_data['sexo'],
            raca = validated_data['raca'],
        )
        pet.save()
        if validated_data.get('medicamentos'):
            for dados_medicamento in validated_data['medicamentos']:
                medicamento = Medicamento(pet = pet, **dados_medicamento)
                medicamento.save()
        if validated_data.get('alimentos'):
            for dados_alimento in validated_data['alimentos']:
                alimento = Alimento(pet = pet, **dados_alimento)
                alimento.save()
        if validated_data.get('cuidados_especiais'):
            for dados_cuidado_especial in validated_data['cuidados_especiais']:
                cuidado_especial = CuidadoEspecial(pet = pet, **dados_cuidado_especial)
                cuidado_especial.save()
        return pet

class ListarPetsDoClienteSerializer(serializers.ModelSerializer):
    """Serializador para listar informações sobre os pets de um cliente"""
    categoria = serializers.ReadOnlyField(source = 'categoria.nome')
    porte = serializers.ReadOnlyField(source = 'porte.descricao')
    sexo = serializers.SerializerMethodField()
    class Meta:
        model = Pet
        fields = ('id', 'nome', 'sexo', 'categoria', 'raca', 'porte')

    def get_sexo(self, obj):
        return obj.get_sexo_display()