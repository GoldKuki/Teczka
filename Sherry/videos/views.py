from django.shortcuts import render, redirect
from .models import Video, Comment

# Create your views here.

def index(request):
    return render(request, 'videos/index.html', {'data': Video.objects.all()})

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
            if request.POST.get('like', False):
                pass
            if request.POST.get('dislike', False):
                pass
        else:
            return redirect('login')

    video.views += 1
    video.save()

    comments = Comment.objects.filter(video__id=id)
    data = {
        'video': video,
        'comments': comments,
    }
    return render(request, 'videos/video.html', data)