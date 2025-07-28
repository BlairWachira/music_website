from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('play/<int:song_id>',views.play_song,name='play_song'),
]