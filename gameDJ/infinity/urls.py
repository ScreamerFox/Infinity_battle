from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'infinity'


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_f, name='login_f'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.battle_view, name='dashboard'),
    path('end_game/', views.end_game, name='end_game'),
    path('rating/', views.leaderboard, name='rating'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)