from .models import *


def fight(player_attack, player_defence, enemy_attack, enemy_defence):
    if player_attack == enemy_defence and enemy_attack == player_defence:
        return 'Вы и враг блокируете атаку'

    if player_attack != enemy_defence and enemy_attack != player_defence:
        return 'Урон друг другу'

    if player_attack != enemy_defence and enemy_attack == player_defence:
        return 'Вы наносите урон и блокируете атаку'

    if player_attack == enemy_defence and enemy_attack != player_defence:
        return 'Враг наносит урон и блокирует Вас'

