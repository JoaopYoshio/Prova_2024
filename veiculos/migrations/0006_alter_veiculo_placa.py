# Generated by Django 5.1.1 on 2024-09-17 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veiculos', '0005_remove_veiculo_acessorios_acessorio_veiculo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veiculo',
            name='placa',
            field=models.CharField(max_length=4),
        ),
    ]
