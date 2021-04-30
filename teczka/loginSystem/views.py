from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
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
    if response.method == 'POST':
        u_form = UserUpdateForm(response.POST, instance=response.user)
        p_form = ProfileUpdateForm(response.POST, response.FILES, instance=response.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=response.user)
        p_form = ProfileUpdateForm(instance=response.user.profile)

    data = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(response, "loginSystem/profile.html", data)