from django.shortcuts import render
from app_music.models import Album, Track


def home(request):
    ctx = {}
    ctx['album'] = album = Album.objects.first()
    ctx['tracks'] = tracks = Track.objects.filter(album=album)
    ctx['tracks_count'] = len(tracks)
    return render(request, 'home.html', ctx)
