# Generated by Django 4.2.4 on 2023-09-20 01:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_remove_version_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='version',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.product'),
        ),
    ]