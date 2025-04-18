# Generated by Django 4.2.8 on 2025-01-14 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0074_generatedapp_api_key"),
    ]

    operations = [
        migrations.CreateModel(
            name="FileInfo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("path", models.URLField()),
                ("info", models.CharField(max_length=255)),
            ],
        ),
    ]
