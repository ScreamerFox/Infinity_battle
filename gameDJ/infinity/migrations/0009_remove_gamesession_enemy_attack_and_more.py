# Generated by Django 5.1.4 on 2024-12-20 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infinity', '0008_remove_gamesession_result'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gamesession',
            name='enemy_attack',
        ),
        migrations.RemoveField(
            model_name='gamesession',
            name='enemy_def',
        ),
        migrations.RemoveField(
            model_name='gamesession',
            name='player_attack',
        ),
        migrations.RemoveField(
            model_name='gamesession',
            name='player_def',
        ),
    ]