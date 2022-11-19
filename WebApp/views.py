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
def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        if request.POST.get("form_type") == 'Sign up':
            form = SignupForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account created for '+ request.POST['username'])
                return redirect('login')
    context = {'form':form}
    return render (request, 'signup.html', context)

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

@login_required(login_url='login')
def requestLabour(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        quantity = request.POST.get('quantity', '')
        work = request.POST.get('work', '')
        date = request.POST.get('date', '')
        requestlabour = RequestLabour(name=name, email=email, phone=phone, quantity=quantity, work_type=work, date=date)
        requestlabour.save()
        return redirect('req2')
    return render(request, 'requestlabour.html')

def request2(request):
    return render(request, 'request2.html')

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        query = request.POST.get('query', '')
        contact = Contact(name=name, email=email, query=query)
        contact.save()
    return render(request, 'home.html')

class RequestLabourCreateView(CreateView):
    model = RequestLabour
    form_class = RequestLabourForm