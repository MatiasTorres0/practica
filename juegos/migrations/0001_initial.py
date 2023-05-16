# Generated by Django 4.1.4 on 2023-02-02 15:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Juego',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
                ('id_tipo_juego', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tipo_juego')),
            ],
        ),
        migrations.CreateModel(
            name='Trivia',
            fields=[
                ('id_trivia', models.AutoField(primary_key=True, serialize=False)),
                ('ordinal', models.CharField(max_length=100)),
                ('pregunta_trivia', models.CharField(max_length=100)),
                ('respuesta_trivia', models.CharField(max_length=100, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sopa_letra',
            fields=[
                ('id_sopa', models.AutoField(primary_key=True, serialize=False)),
                ('pregunta_sopa', models.CharField(max_length=100)),
                ('word', models.CharField(max_length=50)),
                ('direction', models.CharField(max_length=50)),
                ('start', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Resultado_juego',
            fields=[
                ('id_resultado', models.AutoField(primary_key=True, serialize=False)),
                ('resultado_1', models.CharField(max_length=100)),
                ('resultado_2', models.CharField(max_length=100)),
                ('resultado_3', models.CharField(max_length=100)),
                ('resultado_4', models.CharField(blank=True, max_length=100, null=True)),
                ('resultado_5', models.CharField(blank=True, max_length=100, null=True)),
                ('timestampp', models.DateTimeField(auto_now_add=True)),
                ('id_juego', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='juegos.juego')),
                ('id_usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]