from django.shortcuts import render, redirect

from profiles.models import Profile
from .models import Video, Comment, Playlist
from .forms import CommentCreationForm


# Create your views here.

def index(request):
    if request.user.is_authenticated:
        playlists = request.user.profile.playlist_set.all()
    else:
        playlists = None

    data = {
        'videos': Video.objects.all(),
        'playlists': playlists,
    }
    return render(request, 'videos/index.html', data)

def search(request):
    if request.method == 'POST':
        looking_for = request.POST.get('in_search', False)
        if looking_for:
            titile = Video.objects.filter(title__contains=looking_for)
            description = Video.objects.filter(description__contains=looking_for)
            results = titile # .union(description)
            return render(request, 'videos/search.html', {'data': results})

    return render(request, 'videos/search.html', {})

def video(request, id):
    video = Video.objects.filter(id=id).first()
    if video is None:
        return redirect('index')

    if request.method == 'POST':
        if request.user.is_authenticated:

            user = request.user
            profile = Profile.objects.filter(user=user).first()

            if request.POST.get('comment', False):
                content = request.POST.get('content', '')
                if not content == '':
                    Comment.objects.create(author=profile, video=video, content=content)

            like_pl = Playlist.objects.filter(author=profile, titile='Liked').first()
            dislike_pl = Playlist.objects.filter(author=profile, titile='Disliked').first()
            in_like_pl = video in like_pl.videos.all()
            in_dislike_pl = video in dislike_pl.videos.all()
            if request.POST.get('like', False):
                if in_like_pl:
                    like_pl.videos.remove(video)
                    video.likes -= 1
                else:
                    like_pl.videos.add(video)
                    like_pl.save()
                    video.likes += 1

                if in_dislike_pl:
                    dislike_pl.videos.remove(video)
                    video.dislikes -= 1
                
            if request.POST.get('dislike', False):
                
                if in_dislike_pl:
                    dislike_pl.videos.remove(video)
                    video.dislikes -= 1
                else:
                    dislike_pl.videos.add(video)
                    dislike_pl.save()
                    video.dislikes += 1
                    
                if in_like_pl:
                    like_pl.videos.remove(video)
                    video.likes -= 1
        else:
            return redirect('login')
        # zle ify ułożone, autoryzacja przed kliknieciem like badz dislike

    video.views += 1
    video.save()

    tags = video.tags.all()

    comments = Comment.objects.filter(video__id=id)
    data = {
        'video': video,
        'tags': tags,
        'comments': comments,
    }
    return render(request, 'videos/video.html', data)

def playlist(request, id):
    playlist = Playlist.objects.filter(id=id).first()

    if playlist is None:
        return redirect('index')

    if not playlist.author.id == request.user.profile.id:
        return redirect('index')
    
    data = {
        'playlist': playlist,
        'videos': playlist.videos.all(),
        'playlists': request.user.profile.playlist_set.all(),
    }

    return render(request, 'videos/playlist.html', data)
