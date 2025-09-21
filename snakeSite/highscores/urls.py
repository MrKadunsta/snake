from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('home/', views.main, name='main'),
    path('fullscreen/', views.fullscreen, name='fullscreen'),
    path('highscores/', views.highscores, name='highscores'),
    path('game/', views.game, name='game'),
    path('check-highscore/', views.check_highscore, name='check_highscore'),
    path('save-highscore/', views.save_highscore, name='save_highscore'),
    path('about/', views.about, name='about'),
    path('how-to-play', views.htp, name='htp')
]