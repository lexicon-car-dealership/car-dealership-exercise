from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Adjust redirect as needed
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'authentication/login.html')

def user_logout(request):
    logout(request)
    return redirect('home')  # Adjust redirect as needed

def user_register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('user_login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'authentication/register.html', {'form': form})
