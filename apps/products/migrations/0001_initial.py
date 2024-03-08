# Generated by Django 5.0.3 on 2024-03-08 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('product_type', models.CharField(choices=[('EL', 'Electronics'), ('CL', 'Clothing'), ('FD', 'Food')], max_length=255)),
                ('size', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
    ]