# Generated by Django 5.1.1 on 2024-09-17 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veiculos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acessorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='anoFabricacao',
            field=models.CharField(max_length=20),
        ),
    ]
