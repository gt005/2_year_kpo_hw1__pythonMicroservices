# Generated by Django 4.2.1 on 2023-05-25 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0002_remove_dish_is_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='orderdish',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
    ]
