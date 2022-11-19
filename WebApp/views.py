from django.shortcuts import render, redirect
from .decorators import unauthenticated_user
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'base.html')

@login_required(login_url='login')
def profile(request):
    return render(request, 'profile.html')

@unauthenticated_user
def login_user(request):
    if not request.user.is_authenticated :
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('home')

def course(request):
    return render(request, 'course.html')