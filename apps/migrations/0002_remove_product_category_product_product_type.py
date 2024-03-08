# Generated by Django 5.0.3 on 2024-03-07 07:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="category",
        ),
        migrations.AddField(
            model_name="product",
            name="product_type",
            field=models.CharField(
                choices=[("EL", "Electronics"), ("CL", "Clothing"), ("FD", "Food")],
                default="EL",
                max_length=255,
            ),
        ),
    ]
