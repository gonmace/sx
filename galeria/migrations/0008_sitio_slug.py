# Generated by Django 4.2.11 on 2024-06-09 20:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("galeria", "0007_remove_sitio_slug_alter_sitio_sitio"),
    ]

    operations = [
        migrations.AddField(
            model_name="sitio",
            name="slug",
            field=models.SlugField(blank=True, max_length=10, null=True),
        ),
    ]
