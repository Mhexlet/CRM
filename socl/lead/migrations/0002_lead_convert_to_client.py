# Generated by Django 4.1.7 on 2023-03-29 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='convert_to_client',
            field=models.BooleanField(default=False),
        ),
    ]
