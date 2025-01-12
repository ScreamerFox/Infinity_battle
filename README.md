<h1 align="center">Игра рогалик <a href="https://github.com/ScreamerFox/Infinity_battle" target="_blank">Infinity battle ⚔️</a>
</br>
<img src="https://github.com/ScreamerFox/Infinity_battle/blob/master/gameDJ/media/images/sis/preview.jpg" height="500"/>

<h2 align="center">О Проекте:</h2>
<h3> Веб-игра на Django, где игрок сражается с монстрами, повышает уровень и набирает очки.
Вам предстоит сразиться с большим количеством врагов и занять первую строчку в рейтинге лучших.
Но даже это не всё. Ведь её нужно ещё и удержать</h3>

<h2>Технологии</h2>

<ul>
    <li>Python 3.12</li>
    <li>Django</li>
    <li>Bootstrap</li>
</ul>

<h2 align="center">Об игре:</h2>
<h3>Вы играете за обычного воина что сражается с монстрами, дабы очистить сей белый свет от нечисти!
Ваша задача проста:
  Одолеть столько монстров сколько сможете.</h3>

<h2 align="center">Как играть?</h2>
Для того что бы играть у вас на компьютере должен быть установлен Python версией 3.10 и выше!!!
<h3>этап первый - Установка:</h3>



 1) создайте пустую папку где будет размещаться игра и откройте её в командной строке
 2) скопируйте проект себе на пк командой - `git clone https://github.com/ScreamerFox/Infinity_battle.git`
 3) перейти в папку проекта с помощью команды - `cd Infinity_battle`
 4) Создайте виртуальное окружение:
  
    `python3 -m venv venv (Linux/macOS)`
    
    `python -m venv venv (Windows)`
 5) Активируйте виртуальное окружение:
  
    `source venv/bin/activate (Linux/macOS)`
    
    `venv\Scripts\activate (Windows) `
 6) перейдите в папку gameDJ - `cd gameDJ`
 7) Установите зависимости: - `pip install -r requirements.txt`

<h2 align="center">этап второй - Запуск игры:</h2>
Важно! Убедитесь что вы находитесь в папке с файлом manage.py

1) после всех выполненных ранее шагов вписать - `python manage.py runserver`
если всё - ок, то результат следующий:<img src="https://github.com/ScreamerFox/Infinity_battle/blob/master/gameDJ/media/images/sis/powershell_5SoUnrbcOe.png" height="150"/>
2) копируем и и вставляем ссылку в браузере - `http://127.0.0.1:8000/`
 видим главную страницу игры:<img src="https://github.com/ScreamerFox/Infinity_battle/blob/master/gameDJ/media/images/sis/home_non_auturize.png" height="200"/>
3) если это первый запуск и вы не зарегистрированы то смело жмакаем по кнопке регистрация если же нет, то по кнопке `войти в игру`.
4) проходим простую форму регистрации:
   
    Никнейм: только буквы, цифры и @ . + - _
   
    Пароль: Не делайте пароль похожий на никнейм, минимум 8 символов, не делайте легкие пароли (qwertyuio, abcd1234), и он не может быть только из цифр!
   
   <img src="https://github.com/ScreamerFox/Infinity_battle/blob/master/gameDJ/media/images/sis/register.png" height="200"/>

6) Как только вы зарегистрировались, вас кидает на главную страницу и там уже жмём - `Вперёд в битву!`
7) Мы попадаем на страницу игры. Что мы тут увидим?<img src="https://github.com/ScreamerFox/Infinity_battle/blob/master/gameDJ/media/images/sis/browser_HTxTCnhBbi.png" height="400"/>

<h2 align="center">этап третий - Играем:</h2>
Вы играете за героя, изначально у вас 3 жизни (можно увидеть на скрине)

Бой состоит из следующих действий:
1) Выбор части тела которую будете защищать (область под вашим профилем)
2) Выбор части тела в которую будете бить (область под профилем варага)
3) Жмем подтвердить в окне результатов (среднее окно)
4) В среднем окне появится результат:
     1) ваши действия
     2) действия врага
     3) результат битвы
   
   <img src="https://github.com/ScreamerFox/Infinity_battle/blob/master/gameDJ/media/images/sis/browser_lmwY1ZXsqd.png" height="200"/>

<h2 align="center">Победа?</h2>
Если вы победили, то увидите следующее:
<img src="https://github.com/ScreamerFox/Infinity_battle/blob/master/gameDJ/media/images/sis/notification.png" height="200"/>
Восклицаем "Ура!" и идём к следующему :)

<h2 align="center">Проиграли?</h2>
Если проиграли, увидите:
<img src="https://github.com/ScreamerFox/Infinity_battle/blob/master/gameDJ/media/images/sis/defeat.png" height="200"/>
закрываем уведомление, далее видим это:
<img src="https://github.com/ScreamerFox/Infinity_battle/blob/master/gameDJ/media/images/sis/new_game.png" height="200"/>
Выбираем, играть заново или идём на главный экран.

<h2 align="center">Слава и почёт</h2>
В игре есть доска почёта, где имена десяти лучших войнов высечены навсегда! (ну или пока вас не свергнут более удчливые)
<img src="https://github.com/ScreamerFox/Infinity_battle/blob/master/gameDJ/media/images/sis/hero_board.png" height="200"/>


<h2 align="center">На этом пока всё, но что ждёт нас дальше?</h2>
Планы на будущее:

 1) добавить боссов
 2) добавить систему перков и навыков
 3) добавить реплики мобам
 4) переработать дизайн
 5) добавить меню параметров игры
 6) возможно появится система прокачки персонажа
 7) рассмотреть переезд на другую платформу (мобильное приложение или бот)

<h4>В дальнейшем хотелось бы чтоб проект перерос во что то большее.</h4>

<h2 align="center">Об авторе:</h2>
<h3>Меня зовут Евгений! Я начинающий python-разработчик из Челябинска. мне 29 лет.</h3>

[![GitHub Streak](https://github-readme-streak-stats.herokuapp.com/?user=ScreamerFox)](https://git.io/streak-stats)
