# Generated by Django 4.2.4 on 2023-09-19 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_product_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discription',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='Описание'),
        ),
    ]
