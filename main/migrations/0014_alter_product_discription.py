# Generated by Django 4.2.4 on 2023-09-19 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_product_discription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discription',
            field=models.TextField(max_length=200, verbose_name='Описание продукта'),
        ),
    ]