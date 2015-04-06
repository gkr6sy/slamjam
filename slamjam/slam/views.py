from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'slam/index.html')
def about(request):
    return render(request, 'slam/about.html')
def signup(request):
    return render(request, 'slam/signup.html')