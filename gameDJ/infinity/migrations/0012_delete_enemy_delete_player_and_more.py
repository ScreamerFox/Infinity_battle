# Generated by Django 5.1.4 on 2024-12-21 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infinity', '0011_enemy_player_gamesession_enemy_attack_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Enemy',
        ),
        migrations.DeleteModel(
            name='Player',
        ),
        migrations.RemoveField(
            model_name='gamesession',
            name='enemy_name',
        ),
        migrations.AlterField(
            model_name='gamesession',
            name='enemy_attack',
            field=models.CharField(blank=True, choices=[('голова', 'Head'), ('торс', 'Torso'), ('ноги', 'Legs')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='gamesession',
            name='enemy_defense',
            field=models.CharField(blank=True, choices=[('голова', 'Head'), ('торс', 'Torso'), ('ноги', 'Legs')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='gamesession',
            name='player_attack',
            field=models.CharField(blank=True, choices=[('голова', 'Head'), ('торс', 'Torso'), ('ноги', 'Legs')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='gamesession',
            name='player_defense',
            field=models.CharField(blank=True, choices=[('голова', 'Head'), ('торс', 'Torso'), ('ноги', 'Legs')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='gamesession',
            name='player_hp',
            field=models.PositiveIntegerField(default=10),
        ),
    ]