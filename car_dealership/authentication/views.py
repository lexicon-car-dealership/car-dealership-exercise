from django.contrib.auth import logout
from .forms import EditProfileForm
from django.contrib.auth.forms import UserChangeForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from cars.views import index


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


@login_required
def profile_view(request, profile_id=None):
    # If a profile_id is provided, get the user with that id. Otherwise, get the current user
    if profile_id:
        user = get_object_or_404(User, id=profile_id)
    else:
        user = request.user
    # Initialize the form and accept the none value
    form = None
    # Only allow the user to edit their own profile or allow superusers to edit any profile
    if request.user.is_superuser or request.user == user:
        if request.method == 'POST':
            form = EditProfileForm(request.POST, instance=user, user=user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Profile updated successfully.')
                return redirect('profile', profile_id=user.id)
            else:
                messages.error(request, 'Please correct the error below.')
        else:
            form = EditProfileForm(instance=user, user=user)

    return render(request, 'profile.html', {'form': form, 'user': user, 'current_user': request.user})



def logout_view(request):
    logout(request)
    return redirect('index')
