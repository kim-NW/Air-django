# Generated by Django 4.1.7 on 2023-04-04 14:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("medias", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="photo",
            name="file",
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name="viedo",
            name="file",
            field=models.URLField(),
        ),
    ]
