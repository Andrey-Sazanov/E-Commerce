# Generated by Django 3.2.9 on 2022-07-14 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_rename_img_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]
