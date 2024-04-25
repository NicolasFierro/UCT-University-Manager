# Generated by Django 5.0.2 on 2024-04-11 20:22

import datetime
import django.db.models.deletion
from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=150)),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('password', models.TextField()),
                ('phone', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Artículo',
                'verbose_name_plural': 'Artículos',
            },
        ),
        migrations.CreateModel(
            name='Careers',
            fields=[
                ('idClass', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID de Carrera')),
                ('nameClass', models.CharField(max_length=100, verbose_name='Nombre de la Carrera')),
                ('durationClass', models.IntegerField(verbose_name='Duración en Semestres')),
                ('creditClass', models.IntegerField(verbose_name='Créditos')),
            ],
            options={
                'verbose_name': 'Carrera',
                'verbose_name_plural': 'Carreras',
                'ordering': ['idClass'],
            },
        ),
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=110)),
                ('description', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='LoginAdmins',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=110)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='LoginStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=110)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=30)),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10, unique=True)),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('creditos', models.IntegerField()),
                ('fecha_creacion', models.DateTimeField(default=datetime.datetime.now)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miApp.carrera')),
                ('profesores', models.ManyToManyField(to='miApp.profesor')),
            ],
        ),
    ]
