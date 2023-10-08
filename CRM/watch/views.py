from django.shortcuts import render
from .models import models
from django.views.generic import ListView
from .models import *
# Create your views here.

def homepage(request):
    return render(request,'homepage.html')

def aboutpage(request):
    return render(request,'about')

def contactpage(request):
    return render(request,'contact')
