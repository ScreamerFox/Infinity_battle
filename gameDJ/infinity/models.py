from django.db import models
from django.contrib.auth.models import User

TARGET = [
    ('голова', 'Head'),
    ('торс', 'Torso'),
    ('ноги', 'Legs')
]

enemys = {'Гнолл': 'images/Monsters/гнолл.png',
          'Гаргулия': 'images/Monsters/гаргулия.png',
          'Разбойник': 'images/Monsters/разбойник.png',
          'Вор': 'images/Monsters/вор.png',
          'Крыса': 'images/Monsters/крыса.png',
          'Волк': 'images/Monsters/волк.png',
          'Минотавр': 'images/Monsters/минотавр.png',
          'Кентавр': 'images/Monsters/кентавр.png',
          'Ихтиозавр': 'images/Monsters/ихтиозавр.png',
          'Крылатая бестия': 'images/Monsters/крылан.png',
          'Лупоглаз': 'images/Monsters/лупоглаз.png',
          'Рогач': 'images/Monsters/рогач.png'}


class GameSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    level = models.PositiveIntegerField(default=1)
    player_hp = models.PositiveIntegerField(default=10)
    player_scores = models.PositiveIntegerField(default=0)
    player_attack = models.CharField(max_length=10, choices=TARGET,
                                     null=True, blank=True)
    player_defense = models.CharField(max_length=10, choices=TARGET,
                                      null=True, blank=True)

    enemy_hp = models.PositiveIntegerField(default=1)
    enemy_attack = models.CharField(max_length=10, choices=TARGET,
                                    null=True, blank=True)
    enemy_defense = models.CharField(max_length=10, choices=TARGET,
                                     null=True, blank=True)


class Rating(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='score')
    high_score = models.IntegerField(default=0)
