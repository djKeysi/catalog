# Generated by Django 4.2.4 on 2023-09-20 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_remove_version_product_version_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='flag_of_the_current_version',
            field=models.BooleanField(default=False, verbose_name='признак текущей версии'),
        ),
    ]