from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(response):
    if response.method == 'POST':
        form = UserRegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserRegisterForm()

    return render(response, "loginSystem/register.html", {'form': form})

@login_required
def profile(response):
    return render(response, "loginSystem/profile.html", {})