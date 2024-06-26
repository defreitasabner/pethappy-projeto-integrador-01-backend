# Generated by Django 5.0.4 on 2024-04-23 21:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pessoas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('descricao', models.CharField(max_length=300, verbose_name='Descrição')),
            ],
        ),
        migrations.CreateModel(
            name='Porte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100, verbose_name='Descrição')),
                ('peso_min', models.IntegerField(unique=True, verbose_name='Peso Mínimo')),
                ('peso_max', models.IntegerField(unique=True, verbose_name='Peso Máximo')),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome da Categoria')),
                ('data_nascimento', models.DateField(verbose_name='Data de Nascimento / Adoção')),
                ('sexo', models.CharField(choices=[('F', 'Fêmea'), ('M', 'Macho'), ('I', 'Indeterminado')], default='I', max_length=1, verbose_name='Sexo do Pet')),
                ('raca', models.CharField(blank=True, max_length=100, verbose_name='Raça do Pet')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pets', to='pets.categoria', verbose_name='Categoria do Pet')),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pets', to='pessoas.cliente', verbose_name='Tutor do Pet')),
                ('veterinario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='pets', to='pessoas.veterinario', verbose_name='Veterinário')),
                ('porte', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pets', to='pets.porte', verbose_name='Porte do Pet')),
            ],
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome do Medicamento')),
                ('posologia', models.CharField(help_text='Informações sobre horário, frequência e quantidades das doses.', max_length=300, verbose_name='Posologia')),
                ('observacoes', models.CharField(blank=True, max_length=300, verbose_name='Outras Observações')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medicamentos', to='pets.pet', verbose_name='Pet')),
            ],
        ),
        migrations.CreateModel(
            name='CuidadoEspecial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('O', 'Outros'), ('D', 'Doença'), ('E', 'Emocional')], default='O', max_length=1, verbose_name='Tipo de Cuidado')),
                ('descricao', models.CharField(max_length=300, verbose_name='Descrição do Cuidado Especial')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cuidados_especiais', to='pets.pet', verbose_name='Pet')),
            ],
        ),
        migrations.CreateModel(
            name='Alimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=150, verbose_name='Descrição do Alimento (Nome)')),
                ('quantidade', models.CharField(max_length=150, verbose_name='Descrição da Quantidade')),
                ('periodo', models.CharField(max_length=100, verbose_name='Período')),
                ('local', models.CharField(max_length=300, verbose_name='Local')),
                ('observacoes', models.CharField(blank=True, max_length=300, verbose_name='Outras Observações')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alimentos', to='pets.pet', verbose_name='Pet')),
            ],
        ),
    ]
