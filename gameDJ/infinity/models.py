from django.db import models
from django.contrib.auth.models import User




class GameSession(models.Model):
    RESULT_CHOICES = [
        ('Урон врагу', 'ap_vs_e'),
        ('Урон вам', 'ae_vs_p'),
        ('Вы блокируете', 'bp_vs_e'),
        ('Враг блокирует', 'be_vs_p'),
        ('урон друг другу', 'ap_vs_ae'),
        ('вы и враг блок', 'be_vs_bp'),
    ]

    PART_CHOICES = [
        ('голова', 'Head'),
        ('торс', 'Torso'),
        ('ноги', 'Legs'),
    ]

    level = models.PositiveIntegerField(default=1)
    player_hp = models.PositiveIntegerField(default=3)
    player_scores = models.PositiveIntegerField(default=0)
    player_attack = models.CharField(max_length=10, choices=PART_CHOICES)
    player_def = models.CharField(max_length=10, choices=PART_CHOICES)

    enemy_hp = models.PositiveIntegerField(default=1)
    enemy_attack = models.CharField(max_length=10, choices=PART_CHOICES)
    enemy_def = models.CharField(max_length=10, choices=PART_CHOICES)
    result = models.CharField(max_length=20, choices=RESULT_CHOICES)


    def __str__(self):
        return (f"GameSession({self.player_hp}, Result: {self.result}),"
                f" Level - {self.level}, Scores - {self.player_scores}")

class Rating(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='score')
    high_score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username}: {self.high_score}"
