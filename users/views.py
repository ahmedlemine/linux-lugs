from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForme
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Profile

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created. You can edit your profile, join or add LUGs')
            new_user = authenticate(username=form.cleaned_data['username'],
                        password=form.cleaned_data['password1'],
                        )
            login(request, new_user)
            return redirect('public-profile', username=new_user)
         
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form, 'title': 'Register'})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForme(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your profile has been updated')
            return redirect('public-profile', username=request.user)
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForme(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/edit_profile.html', context)


def user_public_profile(request, username):
    user_public = get_object_or_404(User, username=username)
    user_lugs = user_public.profile.lugs.all()
    context = {
        'user_public': user_public,
        'user_lugs': user_lugs
    }
    return render(request, 'users/user_public_profile.html', context)
