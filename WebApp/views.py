from django.shortcuts import render, redirect
from .decorators import unauthenticated_user
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from .models import * 
from .forms import * 

def home(request):
    if request.user.is_authenticated :
        return redirect('user')
    return render(request, 'home.html')

@login_required(login_url='login')
def profile(request):
    return render(request, 'profile.html')

@login_required(login_url='login')
def user(request):
    return render(request, 'user.html')

@unauthenticated_user
def login_user(request):
    if not request.user.is_authenticated :
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('user')
            else:
                messages.info(request, 'Username OR password is incorrect')
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('home')

class RequestLabourCreateView(CreateView):
    model = RequestLabour
    form_class = RequestLabourForm