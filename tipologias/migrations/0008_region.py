# Generated by Django 4.1.4 on 2023-02-02 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tipologias', '0007_remove_provincia_id_region'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id_region', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_region', models.CharField(max_length=100)),
            ],
        ),
    ]