from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from .forms import SignupForm, LoginForm, SearchForm
from django.http import HttpResponseRedirect

# Create your views here.


def home(request):
    return render(request, 'slam/index.html')


def about(request):
    return render(request, 'slam/about.html')


def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST, request.FILES)
        if form.is_valid():
            if request.FILES:
                # music = request.FILES['song']
                # This is where we'd input the song into the system for parsing
                print("We got a song")
                url = 'http://soundcloud.com/forss/sets/soulhack'
                return render(request, 'slam/results.html', {"url": url})
    else:
        form = SearchForm()
    return render(request, 'slam/search.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(form['username'].value(), form['username'].value(), form['password'].value())
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            auth_login(request, user)
            print("Successfully logged in as " + user.username)
            return HttpResponseRedirect('/')
    else:
        form = SignupForm()
    return render(request, 'slam/signup.html', {'form':form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return HttpResponseRedirect('/')
            else:
                print("Invalid Login")
    else:
        form = LoginForm()
    return render(request, 'slam/login.html', {'form':form})


def exit(request):
    logout(request)
    print("Successfully logged out.")
    return HttpResponseRedirect('/')

