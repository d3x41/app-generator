# Generated by Django 4.2.8 on 2024-11-13 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0066_prompt_response"),
    ]

    operations = [
        migrations.DeleteModel(
            name="APIKey",
        ),
    ]
