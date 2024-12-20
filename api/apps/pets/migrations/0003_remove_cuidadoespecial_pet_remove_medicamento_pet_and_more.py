# Generated by Django 5.0.4 on 2024-11-02 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_auto_20240423_1800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cuidadoespecial',
            name='pet',
        ),
        migrations.RemoveField(
            model_name='medicamento',
            name='pet',
        ),
        migrations.AddField(
            model_name='pet',
            name='alimentos',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='Descrição da Alimentação'),
        ),
        migrations.AddField(
            model_name='pet',
            name='cuidados_especiais',
            field=models.TextField(blank=True, null=True, verbose_name='Observações'),
        ),
        migrations.AddField(
            model_name='pet',
            name='medicamentos',
            field=models.TextField(blank=True, null=True, verbose_name='Descrição dos medicamentos'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='veterinario',
            field=models.TextField(blank=True, null=True, verbose_name='Veterinário'),
        ),
        migrations.DeleteModel(
            name='Alimento',
        ),
        migrations.DeleteModel(
            name='CuidadoEspecial',
        ),
        migrations.DeleteModel(
            name='Medicamento',
        ),
    ]
