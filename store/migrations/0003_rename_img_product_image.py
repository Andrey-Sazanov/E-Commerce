# Generated by Django 3.2.9 on 2022-07-13 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='img',
            new_name='image',
        ),
    ]
