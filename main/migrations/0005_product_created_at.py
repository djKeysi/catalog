# Generated by Django 4.2.4 on 2023-09-03 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_category_discription_alter_category_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.CharField(default=1, max_length=100, verbose_name='Создание'),
            preserve_default=False,
        ),
    ]