# Generated by Django 4.1.4 on 2023-02-02 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_usuario_tipo_usuario'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tipo_usuario',
        ),
    ]
