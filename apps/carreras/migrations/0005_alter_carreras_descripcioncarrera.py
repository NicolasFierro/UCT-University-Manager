# Generated by Django 5.0.3 on 2024-06-04 22:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carreras', '0004_alter_carreras_descripcioncarrera'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carreras',
            name='DescripcionCarrera',
            field=models.TextField(validators=[django.core.validators.MinLengthValidator(100), django.core.validators.MaxLengthValidator(100)], verbose_name='Descripcion de la Carrera'),
        ),
    ]