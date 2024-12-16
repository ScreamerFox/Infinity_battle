# Generated by Django 5.1.4 on 2024-12-07 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infinity', '0002_alter_gamesession_enemy_part_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gamesession',
            name='player',
        ),
        migrations.AddField(
            model_name='gamesession',
            name='player_hp',
            field=models.PositiveIntegerField(default=3),
        ),
        migrations.DeleteModel(
            name='Hero',
        ),
    ]