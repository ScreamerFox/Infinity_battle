from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login as login_auth
from django.contrib.auth import logout as logout_auth
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

import logging

from .forms import *
from .models import GameSession
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
    level = request.session.get('level', 1)
    player_hp = request.session.get('player_hp', 3)
    player_scores = request.session.get('player_scores', 0)
    enemy = request.session.get('enemy', rand_enemy())
    enemy_hp = request.session.get('enemy_hp', 1)
    username = request.user.username
    notification = None

    hero_img = 'images/Hero.png'
    monster_image = enemys.get(enemy, "images/Monsters/default.png")

    logger.debug(f"Начало боя. Уровень: {level}, HP игрока: {player_hp}, Очки игрока: {player_scores},"
                f" Враг: {enemy}, HP врага: {enemy_hp}")

    if request.method == 'POST':
        player_attack = request.POST.get('player_attack')
        player_def = request.POST.get('player_def')
        logger.debug(f"Действие игрока: Атака - {player_attack}, Защита - {player_def}")

        enemy_attack, enemy_def = generate_enemy_action()
        logger.debug(f"Действие врага: Атака - {enemy_attack}, Защита - {enemy_def}")

        result = fight(player_attack, player_def, enemy_attack, enemy_def)
        logger.info(f"Результат боя: {result}")

        if result == 'Враг наносит урон и блокирует вас' or result == 'Урон друг другу':
            player_hp -= 1
            logger.info(f"Игрок получил урон. HP игрока: {player_hp}")

        if result == 'Вы наносите урон и блокируете атаку' or result == 'Урон друг другу':
            enemy_hp -= 1
        now_enemy = enemy

        if enemy_hp <= 0:
            notification = 'enemy_defeated'
            player_scores += 100
            level += 1
            enemy = rand_enemy()
            monster_image = enemys.get(enemy, "images/Monsters/default.png")
            #enemy_hp = level  # Для повышения сложности)
            enemy_hp = 1
            logger.info(f"Враг {enemy} побежден! Уровень повышен до {level}, очки игрока: {player_scores}")

        if player_hp <= 0:
            notification = 'player_defeated'
            if not notification:
                return redirect('infinity:end_game')
                logger.info("Игрок проиграл.")

        request.session['level'] = level
        request.session['player_hp'] = player_hp
        request.session['player_scores'] = player_scores
        request.session['enemy'] = enemy

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
            'now_enemy': now_enemy
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
    player_scores = request.session.get('player_scores', 0)

    if request.user.is_authenticated:
        player_score, created = Rating.objects.get_or_create(user=request.user)
        if player_scores > player_score.high_score:
            player_score.high_score = player_scores
            player_score.save()

    request.session.pop('level', None)
    request.session.pop('player_hp', None)
    request.session.pop('player_scores', None)
    request.session.pop('enemy', None)
    request.session.pop('enemy_hp', None)

    return render(request, 'end_game.html')

def leaderboard(request):
    top_players = Rating.objects.order_by('-high_score')[:10]  # Топ-10 игроков
    return render(request, 'rating.html', {'top_players': top_players})