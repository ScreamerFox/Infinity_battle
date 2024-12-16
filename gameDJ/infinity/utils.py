from django.shortcuts import render, redirect

from .models import *
import random



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
        'Лупоглаз': 'images/Monsters/лупоглаз.png',
        'Рогач': 'images/Monsters/рогач.png'}

def rand_enemy():
    return random.choice(list(enemys.keys()))

def generate_enemy_action():
    attack = ['голова', 'торс', 'ноги']
    defence = ['голова', 'торс', 'ноги']
    return random.choice(attack), random.choice(defence)



def fight(player_attack, player_defence, enemy_attack, enemy_defence):
    if player_attack == enemy_defence and enemy_attack == player_defence:
        return 'вы и враг блокируете атаку'

    if player_attack != enemy_defence and enemy_attack != player_defence:
        return 'Урон друг другу'

    if player_attack != enemy_defence and enemy_attack == player_defence:
        return 'Вы наносите урон и блокируете атаку'

    if player_attack == enemy_defence and enemy_attack != player_defence:
        return 'Враг наносит урон и блокирует вас'