from rest_framework import serializers
from django.db import transaction
from django.contrib.auth.models import User

from pet_happy.models import Cliente, Telefone, Endereco, Funcionario


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ('id', 'cidade', 'bairro', 'rua', 'numero', 'complemento')

class TelefoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telefone
        fields = ('id', 'numero', 'is_contato_emergencia')

class ClienteSerializer(serializers.ModelSerializer):
    telefones = TelefoneSerializer(many = True)
    endereco = EnderecoSerializer()
    
    class Meta:
        model = Cliente
        fields = ('id', 'nome', 'endereco', 'telefones')
    
    @transaction.atomic
    def create(self, validated_data):
        cliente = Cliente.objects.create(nome = validated_data['nome'])
        endereco = Endereco(cliente = cliente, **validated_data['endereco'])
        endereco.save()
        for dados_telefone in validated_data['telefones']:
            telefone = Telefone(cliente = cliente, **dados_telefone)
            telefone.save()
        return cliente

class UpdateTelefoneSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = Telefone
        fields = ('id', 'numero', 'is_contato_emergencia')

class UpdateClienteSerializer(serializers.ModelSerializer):
    telefones = UpdateTelefoneSerializer(many = True, required = False)
    endereco = EnderecoSerializer(required = False)
    
    class Meta:
        model = Cliente
        fields = ('id', 'nome', 'endereco', 'telefones')

    @transaction.atomic
    def update(self, instance, validated_data):
        if validated_data.get('endereco'):
            endereco = Endereco.objects.filter(cliente = instance)
            endereco.update(**validated_data['endereco'])
            del validated_data['endereco']
        if validated_data.get('telefones'):
            for dados_telefone in validated_data['telefones']:
                if dados_telefone['id'] == 0:
                    del dados_telefone['id']
                    telefone = Telefone(cliente = instance, **dados_telefone)
                    telefone.save()
                elif dados_telefone['id'] == -1:
                    telefone = Telefone.objects.filter(numero = dados_telefone['numero']).first()
                    if telefone:
                        telefone.delete()
                else:
                    telefone = Telefone.objects.filter(id = dados_telefone['id'])
                    telefone.update(**dados_telefone)
            del validated_data['telefones']
        return super().update(instance, validated_data)

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email')
        extra_kwargs = {
            'password': { 'write_only': True }
        }

class FuncionarioSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()
    class Meta:
        model = Funcionario
        fields = ('id', 'nome', 'telefone', 'usuario',)

    @transaction.atomic
    def create(self, validated_data):
        usuario = User.objects.create_user(
            username = validated_data['usuario']['username'],
            password = validated_data['usuario']['password'],
            email = validated_data['usuario']['email'],
        )
        del validated_data['usuario']
        funcionario = Funcionario(usuario =  usuario, **validated_data)
        funcionario.save()
        return funcionario

class UpdateUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('password', 'email')
        extra_kwargs = {
            'password': { 'required': False, 'write_only': True },
            'email': { 'required': False }
        }

class UpdateFuncionarioSerializer(serializers.ModelSerializer):
    usuario = UpdateUsuarioSerializer(required = False)
    class Meta:
        model = Funcionario
        fields = ('nome', 'telefone', 'usuario',)

    @transaction.atomic
    def update(self, instance, validated_data):
        print(validated_data)
        if validated_data['usuario']['email']:
            instance.usuario.email = validated_data['usuario']['email']
        # if validated_data['usuario']['password']:
        #     instance.usuario.set_password(validated_data['usuario']['password'])
        #     instance.usuario.save()
        del validated_data['usuario']
        return super().update(instance, validated_data)