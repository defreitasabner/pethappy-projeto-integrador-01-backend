# Generated by Django 5.0.4 on 2024-04-13 21:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome do Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cidade', models.CharField(max_length=100, verbose_name='Nome da Cidade')),
                ('bairro', models.CharField(max_length=100, verbose_name='Nome do Bairro')),
                ('rua', models.CharField(max_length=100, verbose_name='Nome da Rua')),
                ('numero', models.CharField(max_length=30, verbose_name='Número da Residência')),
                ('complemento', models.CharField(blank=True, max_length=100, verbose_name='Informações Complementares')),
                ('cliente', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='endereco', to='pet_happy.cliente', verbose_name='Endereço do Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=15, verbose_name='Número de Telefone')),
                ('is_contato_emergencia', models.BooleanField(default=False, verbose_name='Contato de Emergência')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='telefones', to='pet_happy.cliente', verbose_name='Cliente')),
            ],
        ),
    ]
