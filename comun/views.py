from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.


def home_view(request):
    return render (request, 'comun/inicio.html')

def about_view(request):
    return render (request, 'comun/about.html')