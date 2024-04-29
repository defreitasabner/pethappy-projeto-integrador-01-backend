from rest_framework import serializers
from django.db import transaction
from django.contrib.auth.models import User

from pessoas.models import *

#TODO: refatorar serializadores para evitar repetição de código
class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ('id', 'cidade', 'bairro', 'rua', 'numero', 'complemento')

class TelefoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telefone
        fields = ('id', 'numero', 'is_contato_emergencia')

class PessoaSerializer(serializers.ModelSerializer):
    telefones = TelefoneSerializer(many = True)
    endereco = EnderecoSerializer()
    class Meta:
        model = Pessoa
        fields = ('id', 'nome', 'endereco', 'telefones')

    @transaction.atomic
    def create(self, validated_data):
        pessoa = Pessoa.objects.create(nome = validated_data['nome'])
        endereco = Endereco(pessoa = pessoa, **validated_data['endereco'])
        endereco.save()
        for dados_telefone in validated_data['telefones']:
            telefone = Telefone(pessoa = pessoa, **dados_telefone)
            telefone.save()
        return pessoa

class UpdateTelefoneSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = Telefone
        fields = ('id', 'numero', 'is_contato_emergencia')

class UpdatePessoaSerializer(serializers.ModelSerializer):
    telefones = UpdateTelefoneSerializer(many = True, required = False)
    endereco = EnderecoSerializer(required = False)
    
    class Meta:
        model = Pessoa
        fields = ('id', 'nome', 'endereco', 'telefones')

class ClienteSerializer(serializers.ModelSerializer):
    pessoa = PessoaSerializer()
    class Meta:
        model = Cliente
        fields = ('id', 'pessoa')

    @transaction.atomic
    def create(self, validated_data):
        pessoa = Pessoa.objects.create(nome = validated_data['pessoa']['nome'])
        endereco = Endereco(pessoa = pessoa, **validated_data['pessoa']['endereco'])
        endereco.save()
        for dados_telefone in validated_data['pessoa']['telefones']:
            telefone = Telefone(pessoa = pessoa, **dados_telefone)
            telefone.save()
        cliente = Cliente.objects.create(pessoa = pessoa)
        return cliente

class UpdateClienteSerializer(serializers.ModelSerializer):
    pessoa = UpdatePessoaSerializer()
    class Meta:
        model = Cliente
        fields = ('id', 'pessoa')

    @transaction.atomic
    def update(self, instance, validated_data):
        if validated_data['pessoa'].get('nome'):
            instance.pessoa.nome = validated_data['pessoa']['nome']
            instance.pessoa.save()
        if validated_data['pessoa'].get('endereco'):
            endereco = Endereco.objects.filter(pessoa = instance.pessoa)
            endereco.update(**validated_data['pessoa']['endereco'])
        if validated_data['pessoa'].get('telefones'):
            for dados_telefone in validated_data['pessoa']['telefones']:
                if dados_telefone['id'] == 0:
                    del dados_telefone['id']
                    telefone = Telefone(pessoa = instance.pessoa, **dados_telefone)
                    telefone.save()
                elif dados_telefone['id'] == -1:
                    telefone = Telefone.objects.filter(numero = dados_telefone['numero']).first()
                    if telefone:
                        telefone.delete()
                else:
                    telefone = Telefone.objects.filter(id = dados_telefone['id'])
                    telefone.update(**dados_telefone)
        return instance

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email')
        extra_kwargs = {
            'password': { 'write_only': True }
        }

class FuncionarioSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()
    pessoa = PessoaSerializer()
    class Meta:
        model = Funcionario
        fields = ('id', 'usuario', 'pessoa')

    @transaction.atomic
    def create(self, validated_data):
        usuario = User.objects.create_user(
            username = validated_data['usuario']['username'],
            password = validated_data['usuario']['password'],
            email = validated_data['usuario']['email'],
        )
        pessoa = Pessoa.objects.create(nome = validated_data['pessoa']['nome'])
        endereco = Endereco(pessoa = pessoa, **validated_data['pessoa']['endereco'])
        endereco.save()
        for dados_telefone in validated_data['pessoa']['telefones']:
            telefone = Telefone(pessoa = pessoa, **dados_telefone)
            telefone.save()
        funcionario = Funcionario.objects.create(usuario = usuario, pessoa = pessoa)
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
    pessoa = UpdatePessoaSerializer(required = False)
    class Meta:
        model = Funcionario
        fields = ('usuario', 'pessoa')

    @transaction.atomic
    def update(self, instance, validated_data):
        if validated_data['usuario'].get('email'):
            instance.usuario.email = validated_data['usuario']['email']
        # if validated_data['usuario']['password']:
        #     instance.usuario.set_password(validated_data['usuario']['password'])
        #     instance.usuario.save()
        if validated_data['pessoa'].get('nome'):
            instance.pessoa.nome = validated_data['pessoa']['nome']
            instance.pessoa.save()
        if validated_data['pessoa'].get('endereco'):
            endereco = Endereco.objects.filter(pessoa = instance.pessoa)
            endereco.update(**validated_data['pessoa']['endereco'])
        if validated_data['pessoa'].get('telefones'):
            for dados_telefone in validated_data['pessoa']['telefones']:
                if dados_telefone['id'] == 0:
                    del dados_telefone['id']
                    telefone = Telefone(pessoa = instance.pessoa, **dados_telefone)
                    telefone.save()
                elif dados_telefone['id'] == -1:
                    telefone = Telefone.objects.filter(numero = dados_telefone['numero']).first()
                    if telefone:
                        telefone.delete()
                else:
                    telefone = Telefone.objects.filter(id = dados_telefone['id'])
                    telefone.update(**dados_telefone)
        return instance
    
class VeterinarioSerializer(serializers.ModelSerializer):
    pessoa = PessoaSerializer()
    class Meta:
        model = Veterinario
        fields = ('id', 'pessoa', 'clinica')

    @transaction.atomic
    def create(self, validated_data):
        pessoa = PessoaSerializer().create(validated_data = validated_data['pessoa'])
        veterinario = Veterinario.objects.create(pessoa = pessoa, clinica = validated_data['clinica'])
        return veterinario