# Generated by Django 2.1.1 on 2018-09-08 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_active',
            field=models.TextField(default=True),
        ),
    ]
