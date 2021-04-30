from django.shortcuts import render
from .models import Video

# Create your views here.

def index(response):
    data = {
        'videos': Video.objects.all()
    }
    return render(response, "main/index.html", data)