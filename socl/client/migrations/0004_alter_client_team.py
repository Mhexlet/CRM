# Generated by Django 4.1.7 on 2023-03-30 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
        ('client', '0003_rename_teams_client_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clients', to='team.team'),
        ),
    ]
