from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *
from django.shortcuts import render
def display_topic(request):
    qsto=Topic.objects.all()
    d={'qsto':qsto}
    return render(request,'display_topic.html',d)
def display_web(request):
    qswo=Webpage.objects.all()
    d={'qswo':qswo}
    return render(request,'display_web.html',d)