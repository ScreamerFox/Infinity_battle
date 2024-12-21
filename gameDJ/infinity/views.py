from django.shortcuts import render, redirect
from django.contrib.auth import login as login_auth
from django.contrib.auth import logout as logout_auth
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

import logging
import random

from .models import *
from .utils import *

logger = logging.getLogger(__name__)


def home(request):
    username = request.user.username
    context = {
        'username': username,
    }
    return render(request, 'home.html', context)


def register(request):
    logger.info("Начало обработки запроса регистрации.")
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            logger.info("Форма регистрации успешно прошла валидацию.")
            user = form.save()
            logger.info(f"Пользователь {user.username} успешно создан.")
            login_auth(request, user)
            logger.info(f"Пользователь {user.username} успешно залогинен.")
            return redirect('infinity:home')
    else:
        form = UserCreationForm()
        logger.debug("Отображение формы регистрации (метод GET).")
    context = {
        'form': form,
    }
    return render(request, 'register.html', context)  # рендерим)


def login_f(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login_auth(request, user)
            logger.info(f"Пользователь {user.username} успешно авторизован.")
            return redirect('infinity:home')
    else:
        form = AuthenticationForm()
        logger.debug("Отображение формы авторизации (метод GET).")
    context = {
        'form': form,
    }
    return render(request, 'login.html', context)


@login_required
def user_logout(request):
    logout_auth(request)
    return redirect('infinity:login_f')


#game______________________________________________________________________________________________________

def battle_view(request):
    game_session, created = GameSession.objects.get_or_create(user=request.user)
    username = request.user.username
    if created or not request.session.get('initialized', False):
        game_session.level = 1
        game_session.player_hp = 3
        game_session.player_scores = 0
        enemy = random.choice(list(enemys.keys()))
        game_session.enemy_hp = 1
        request.session['enemy'] = enemy
        request.session['initialized'] = True
        game_session.save()
    else:
        enemy = request.session.get('enemy', random.choice(list(enemys.keys())))
        game_session.enemy_hp = game_session.enemy_hp if game_session.enemy_hp > 0 else 1

    level = game_session.level
    player_hp = game_session.player_hp
    player_scores = game_session.player_scores
    enemy_hp = game_session.enemy_hp
    enemy_attack = random.choice(TARGET)[0]
    enemy_def = random.choice(TARGET)[0]
    notification = None

    hero_img = 'images/Hero.png'
    monster_image = enemys.get(enemy, "images/Monsters/default.png")

    if request.method == 'POST':
        player_attack = request.POST.get('player_attack')
        player_def = request.POST.get('player_def')

        result = fight(player_attack, player_def, enemy_attack, enemy_def)

        now_enemy = enemy

        if result == 'Враг наносит урон и блокирует вас' or result == 'Урон друг другу':
            player_hp -= 1

        if result == 'Вы наносите урон и блокируете атаку' or result == 'Урон друг другу':
            enemy_hp -= 1

        if enemy_hp <= 0:
            notification = 'enemy_defeated'
            player_scores += 100
            level += 1
            enemy = random.choice(list(enemys.keys()))
            enemy_hp = 1
            monster_image = enemys.get(enemy, "images/Monsters/default.png")
            request.session['enemy'] = enemy

        if player_hp <= 0:
            notification = 'player_defeated'
            return redirect('infinity:end_game')

        game_session.level = level
        game_session.player_hp = player_hp
        game_session.player_scores = player_scores
        game_session.enemy_hp = enemy_hp
        game_session.save()

        return render(request, 'dashboard.html', {
            'result': result,
            'notification': notification,
            'level': level,
            'username': username,
            'player_hp': player_hp,
            'player_scores': player_scores,
            'player_attack': player_attack,
            'player_def': player_def,
            'hero_img': hero_img,
            'enemy_attack': enemy_attack,
            'enemy_def': enemy_def,
            'enemy': enemy,
            'enemy_hp': enemy_hp,
            'monster_image': monster_image,
            'now_enemy': now_enemy,
        })

    return render(request, 'dashboard.html', {
        'level': level,
        'player_hp': player_hp,
        'player_scores': player_scores,
        'hero_img': hero_img,
        'enemy': enemy,
        'enemy_hp': enemy_hp,
        'monster_image': monster_image,
        'username': username,
    })


def end_game(request):
    game_session, created = GameSession.objects.get_or_create(user=request.user)
    player_scores = game_session.player_scores

    if request.user.is_authenticated:
        player_score, created = Rating.objects.get_or_create(user=request.user)
        logger.debug(f"Current high score: {player_score.high_score}")
        logger.debug(f"Player score: {player_scores}")
        if player_scores > player_score.high_score:
            player_score.high_score = player_scores
            player_score.save()
            logger.info(f"New high score set: {player_score.high_score}")

    game_session.level = 1
    game_session.player_hp = 10
    game_session.player_scores = 0
    game_session.enemy_hp = 1
    request.session['initialized'] = False
    game_session.save()
    logger.info("Game session reset to default values.")

    return render(request, 'end_game.html')


def leaderboard(request):
    top_players = Rating.objects.order_by('-high_score')[:10]  # Топ-10 игроков
    return render(request, 'rating.html', {'top_players': top_players})
