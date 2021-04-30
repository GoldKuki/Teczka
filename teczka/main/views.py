from django.shortcuts import render, redirect
from .models import Video

# Create your views here.

def index(response):
    data = {
        'videos': Video.objects.all()
    }
    return render(response, "main/index.html", data)

def search(request):
    if request.method == 'POST':
        phrase = request.POST.get('search', False)

        if not phrase:
            return render(request, 'main/search.html', {})

        searched = Video.objects.filter(title__contains=phrase)
        data = {
            'results': searched,
        }
        return render(request, 'main/search.html', data)
    else:
        return render(request, 'main/search.html', {})


def video(request, id):
    video = Video.objects.filter(id=id).first()
    if video is None:
        return redirect('index') 
    return render (request, 'main/video.html', {'video': video})