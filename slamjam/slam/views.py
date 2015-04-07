from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from .forms import SignupForm, LoginForm
from django.http import HttpResponseRedirect

# Create your views here.

def home(request):
    return render(request, 'slam/index.html')
def about(request):
    return render(request, 'slam/about.html')
def signup(request):
    if request.method == 'POST':
       form = SignupForm(request.POST)
       if form.is_valid():
          user = User.objects.create_user(form['username'].value(), form['username'].value(), form['password'].value())
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
         user = authenticate(username = username, password = password)
         if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect('/')
         else:
            print("Invalid Login")
    else:
      form = LoginForm()
    return render(request, 'slam/login.html', {'form':form})