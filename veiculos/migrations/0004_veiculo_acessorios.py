# Generated by Django 5.1.1 on 2024-09-17 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veiculos', '0003_alter_veiculo_anofabricacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='veiculo',
            name='acessorios',
            field=models.ManyToManyField(blank=True, to='veiculos.acessorio'),
        ),
    ]
