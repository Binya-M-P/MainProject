# Generated by Django 4.2.5 on 2024-02-09 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page1', '0028_tablereservation_reject'),
    ]

    operations = [
        migrations.AddField(
            model_name='tablereservation',
            name='timeout',
            field=models.TimeField(default=None, null=True),
        ),
    ]
