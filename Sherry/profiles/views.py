from os import access
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages

from .forms import CreateUserForm, ProfileForm
from .models import Profile
from videos.models import Playlist

# Create your views here.

def register(request):
    if request.user.is_authenticated:
        return redirect('index')

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            profile = Profile.objects.create(user=user, nickname=username, background='eb3d3d', 
                                    gender='N', country='N', description='')
            
            Playlist.objects.create(author=profile, access="S", privacy='Pv', title="Liked",
                                    description="Your liked videos on Sharry")
            Playlist.objects.create(author=profile, access="S", privacy='Pv', title="Disliked",
                                    description="Your disliked videos on Sharry")
            Playlist.objects.create(author=profile, access="S", privacy='Pv', title="Watch Later",
                                    description="Your saved videos")

            return redirect('login')

    return render(request, 'profiles/register.html', {'form': form})

def login(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Username or password is incorrect')
            return redirect('login')

    return render(request, 'profiles/login.html', {})

def logout(request):
    auth_logout(request)
    return redirect('login')

def profile(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    
    profile = Profile.objects.filter(id=id).first()
    if profile.privacy == 'Pv' and not profile.id == request.user.profile.id:
        return redirect('index')

    data = {'profile': profile}

    return render(request, 'profiles/profile.html', data)

def edit_profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    profile = request.user.profile

    data = {}

    form = ProfileForm(request.POST or None, request.FILES or None, instance=profile)
    if form.is_valid():
        form.save()
    data['form'] = form

    return render(request, 'profiles/edit_profile.html', data)