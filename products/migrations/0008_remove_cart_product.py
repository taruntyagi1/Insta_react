# Generated by Django 4.1.5 on 2023-01-31 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_cart_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='product',
        ),
    ]
