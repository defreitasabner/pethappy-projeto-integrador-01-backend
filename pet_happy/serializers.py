from rest_framework import serializers
from django.db import transaction

from pet_happy.models import Cliente, Telefone, Endereco


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ('cidade', 'bairro', 'rua', 'numero', 'complemento')

class TelefoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telefone
        fields = ('numero', 'is_contato_emergencia')

class ClienteSerializer(serializers.ModelSerializer):
    telefones = TelefoneSerializer(many = True)
    endereco = EnderecoSerializer()
    
    class Meta:
        model = Cliente
        fields = ('nome', 'endereco', 'telefones')
    
    @transaction.atomic
    def create(self, validated_data):
        cliente = Cliente.objects.create(nome = validated_data['nome'])
        endereco = Endereco(cliente = cliente, **validated_data['endereco'])
        endereco.save()
        for dados_telefone in validated_data['telefones']:
            telefone = Telefone(cliente = cliente, **dados_telefone)
            telefone.save()
        return cliente