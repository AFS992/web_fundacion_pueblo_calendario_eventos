# Generated by Django 4.0.6 on 2022-08-04 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_remove_usuario_telefono_usuario'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AsistenciaUsuario',
        ),
    ]
