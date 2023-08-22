from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *
def d_Topic(request):
    tn=input('enter tname :')
    to=Topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    return HttpResponse('<h1>inserted successfully')
def d_Web(request):
    tn=input('enter tname :')
    to=Topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    n=input('enter name :')
    u=input('enter url :')
    wo=Webpage.objects.get_or_create(topic_name=to,name=n,url=u)[0]
    wo.save()
    return HttpResponse('<h1>inserted successfully')
def d_Acess(request):
    tn=input('enter tname :')
    to=Topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    n=input('enter name :')
    u=input('enter url :')
    wo=Webpage.objects.get_or_create(topic_name=to,name=n,url=u)[0]
    wo.save()
    d=input('enter date :')
    a=input('enter author:')
    ao=Acess.objects.get_or_create(name=wo,date=d,author=a)[0]
    ao.save()
    return HttpResponse('<h1>inserted successfully')