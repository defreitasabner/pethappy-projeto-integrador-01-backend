from rest_framework import serializers, fields
from django.db import transaction

from pets.models import Pet, Categoria, Porte
from pessoas.models import Cliente
from pessoas.serializers import ClienteSerializer

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class PorteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Porte
        fields = '__all__'

class PetSerializer(serializers.ModelSerializer):
    tutor = ClienteSerializer(read_only = True)
    data_nascimento = fields.DateField(input_formats=['%Y-%m-%d', '%Y-%m-%dT%H:%M:%S.%fZ'])
    categoria = CategoriaSerializer(read_only = True)
    porte = PorteSerializer(read_only = True)
    tutor_id = serializers.PrimaryKeyRelatedField(queryset = Cliente.objects.all(), write_only = True)
    categoria_id = serializers.PrimaryKeyRelatedField(queryset = Categoria.objects.all(), write_only = True)
    porte_id = serializers.PrimaryKeyRelatedField(queryset = Porte.objects.all(), write_only = True)
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
        pet = Pet(
            tutor = validated_data.get('tutor_id'),
            categoria = validated_data.get('categoria_id'),
            porte = validated_data.get('porte_id'),
            nome = validated_data.get('nome'),
            data_nascimento = validated_data.get('data_nascimento'),
            sexo = validated_data.get('sexo'),
            raca = validated_data.get('raca'),
            alimentos = validated_data.get('alimentos'),
            medicamentos = validated_data.get('medicamentos'),
            cuidados_especiais = validated_data.get('cuidados_especiais'),
            veterinario = validated_data.get('veterinario'),
        )
        pet.save()
        return pet
    
    @transaction.atomic
    def update(self, instance, validated_data):
        instance.tutor = validated_data.get('tutor_id')
        instance.nome = validated_data.get('nome')
        instance.raca = validated_data.get('raca')
        instance.sexo = validated_data.get('sexo')
        instance.data_nascimento = validated_data.get('data_nascimento')
        instance.categoria = validated_data.get('categoria_id')
        instance.porte = validated_data.get('porte_id')
        instance.alimentos = validated_data.get('alimentos'),
        instance.medicamentos = validated_data.get('medicamentos'),
        instance.cuidados_especiais = validated_data.get('cuidados_especiais'),
        instance.veterinario = validated_data.get('veterinario'),
        instance.save()
        return instance

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