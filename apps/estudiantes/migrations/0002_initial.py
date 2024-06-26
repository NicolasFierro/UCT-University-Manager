# Generated by Django 5.0.3 on 2024-06-03 10:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('estudiantes', '0001_initial'),
        ('materias', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiantes',
            name='materia',
            field=models.ManyToManyField(related_name='estudintes', to='materias.materia'),
        ),
        migrations.AddField(
            model_name='estudiantes',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='estudiantes', to=settings.AUTH_USER_MODEL),
        ),
    ]
