# Generated by Django 5.1.4 on 2024-12-21 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infinity', '0010_gamesession_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enemy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('max_hp', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_hp', models.PositiveIntegerField(default=10)),
            ],
        ),
        migrations.AddField(
            model_name='gamesession',
            name='enemy_attack',
            field=models.CharField(blank=True, choices=[('голова', 'Head'), ('тело', 'Torso'), ('ноги', 'Legs')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='gamesession',
            name='enemy_defense',
            field=models.CharField(blank=True, choices=[('голова', 'Head'), ('тело', 'Torso'), ('ноги', 'Legs')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='gamesession',
            name='enemy_name',
            field=models.CharField(blank=True, choices=[('Гнолл', 'images/Monsters/гнолл.png'), ('Гаргулия', 'images/Monsters/гаргулия.png'), ('Разбойник', 'images/Monsters/разбойник.png'), ('Вор', 'images/Monsters/вор.png'), ('Крыса', 'images/Monsters/крыса.png'), ('Волк', 'images/Monsters/волк.png'), ('Минотавр', 'images/Monsters/минотавр.png'), ('Кентавр', 'images/Monsters/кентавр.png'), ('Ихтиозавр', 'images/Monsters/ихтиозавр.png'), ('Крылатая бестия', 'images/Monsters/крылан.png'), ('Лупоглаз', 'images/Monsters/лупоглаз.png'), ('Рогач', 'images/Monsters/рогач.png')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='gamesession',
            name='player_attack',
            field=models.CharField(blank=True, choices=[('голова', 'Head'), ('тело', 'Torso'), ('ноги', 'Legs')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='gamesession',
            name='player_defense',
            field=models.CharField(blank=True, choices=[('голова', 'Head'), ('тело', 'Torso'), ('ноги', 'Legs')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='gamesession',
            name='player_hp',
            field=models.PositiveIntegerField(default=100),
        ),
    ]