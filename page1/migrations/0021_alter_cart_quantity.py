# Generated by Django 4.2.5 on 2023-11-24 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page1', '0020_order_old'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
