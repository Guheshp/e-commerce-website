# Generated by Django 4.2.1 on 2024-01-19 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_products_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='products',
            new_name='product',
        ),
    ]