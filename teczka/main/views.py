from django.shortcuts import render
from .models import Video

# Create your views here.

def index(response):
    return render(response, "main/index.html", {})