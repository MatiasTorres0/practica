# Generated by Django 4.1.4 on 2023-02-02 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tipologias', '0009_provincia_id_region'),
        ('app', '0010_delete_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='id_comuna',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tipologias.comuna'),
        ),
    ]