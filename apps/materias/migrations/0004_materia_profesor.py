# Generated by Django 5.0.3 on 2024-06-24 19:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materias', '0003_materia_imagenesmateria'),
        ('profesores', '0006_remove_profesor_carrera_remove_profesor_materia'),
    ]

    operations = [
        migrations.AddField(
            model_name='materia',
            name='profesor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Materia_dictadas', to='profesores.profesor'),
        ),
    ]
