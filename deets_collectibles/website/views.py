from django.shortcuts import render

from django.http import HttpResponse
from datetime import datetime

from store.models import Meeting

def welcome(request):
    return render(request, "website/welcome.html")

def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))

def store(request):
    return HttpResponse("Welcome to the store!")