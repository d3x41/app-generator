# Generated by Django 4.2.8 on 2024-11-07 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0061_products_card_info_alter_products_design_css"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="products",
            name="changelog",
        ),
    ]
