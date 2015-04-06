from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .forms import SignupForm
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
          return HttpResponseRedirect('/home/')
    else:
       form = SignupForm()
    return render(request, 'slam/signup.html', {'form':form})
