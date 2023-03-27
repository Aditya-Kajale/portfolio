from django.shortcuts import render
from django.shortcuts import HttpResponse,render

# Create your views here.

def home(request):
    return render(request, 'base/home.html')

def about(request):
    return render(request, 'base/about.html')

def projects(request):
    return render(request, 'base/project.html')

def contact(request):
    return render(request, 'base/contact.html')
