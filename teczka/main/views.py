from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return HttpResponse("<p>siema</p>")

def login(response):
    return HttpResponse("<p>login page</p>")