# Generated by Django 4.2.5 on 2023-10-30 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page1', '0004_person_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='status',
            field=models.BooleanField(blank=True, default='yes', null=True),
        ),
    ]
