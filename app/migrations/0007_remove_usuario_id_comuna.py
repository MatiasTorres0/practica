# Generated by Django 4.1.4 on 2023-02-02 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_usuario_tipo_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='id_comuna',
        ),
    ]
