# Generated by Django 5.1.1 on 2024-09-16 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=50)),
                ('anoFabricacao', models.IntegerField()),
                ('placa', models.CharField(max_length=20)),
            ],
        ),
    ]
