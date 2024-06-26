# Generated by Django 5.0.3 on 2024-06-18 22:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carreras', '0006_alter_carreras_descripcioncarrera'),
        ('estudiantes', '0005_estudiantes_apellido_estudiantes_email_and_more'),
        ('materias', '0002_materia_duraccionmateria'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiantes',
            name='carrera',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estudiantes', to='carreras.carreras'),
        ),
        migrations.AlterField(
            model_name='estudiantes',
            name='materia',
            field=models.ManyToManyField(related_name='estudiantes', to='materias.materia'),
        ),
        migrations.AlterField(
            model_name='estudiantes',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='estudiantes', to=settings.AUTH_USER_MODEL),
        ),
    ]
