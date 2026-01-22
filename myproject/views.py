from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def membership(request):
    return render(request, 'membership.html')