# Generated by Django 5.0.3 on 2024-06-19 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materias', '0002_materia_duraccionmateria'),
        ('profesores', '0004_remove_profesor_materia'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesor',
            name='materia',
            field=models.ManyToManyField(related_name='profesores', to='materias.materia'),
        ),
    ]
