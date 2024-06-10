# Generated by Django 4.2.11 on 2024-06-10 04:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("galeria", "0013_alter_comentario_fecha_carga"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comentario",
            name="fecha_carga",
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="imagen",
            name="fecha_carga",
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
