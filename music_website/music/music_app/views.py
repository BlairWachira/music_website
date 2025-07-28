from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Music

def dashboard(request):
    music_list = Music.objects.all()
    return render(request, 'dashboard.html', {'music_list': music_list})

def play_song(request, song_id):
    song = get_object_or_404(Music, id=song_id)
    return render(request, 'play_song.html', {'song': song})

