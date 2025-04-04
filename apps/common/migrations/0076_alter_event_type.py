# Generated by Django 4.2.8 on 2025-01-19 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0075_fileinfo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="type",
            field=models.CharField(
                choices=[
                    ("GENERAL", "General"),
                    ("ERR_500", "ERR_500"),
                    ("ERR_404", "ERR_404"),
                    ("ERR_403", "ERR_403"),
                    ("ERR_400", "ERR_400"),
                    ("API", "API"),
                    ("CSV_PROCESS", "CSV Processing"),
                    ("DB_MIGRATOR", "DB Migrator"),
                    ("DB_PROCESSOR", "DB Processor"),
                ],
                default="GENERAL",
                max_length=100,
            ),
        ),
    ]
