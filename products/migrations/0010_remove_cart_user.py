# Generated by Django 4.1.5 on 2023-01-31 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_cart_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='user',
        ),
    ]
