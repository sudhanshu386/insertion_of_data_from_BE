from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *

def insert_topic(request):
    tn=input('enter topic_name')

    TO=Topic.objects.get_or_create(topic_name=tn)[0]

    TO.save()
    return HttpResponse('Topic is created successfully')







def insert_webpage(request):
    tn=input('enter tn')
    n=input('enter name')
    u=input('enter url')
    e=input('enter email')

    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()

    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)[0]
    WO.save()

    return HttpResponse('Webpage is Created')









def insert_accessrecord(request):


    tn=input('enter tn')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()

    n=input('enter name')  
    u=input('enter url')
    e=input('enter email') 

    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)[0]
    WO.save()   
    d=input('enter date')
    a=input('enter author')

    AO=AccessRecord.objects.get_or_create(name=WO,date=d,author=a)[0]
    AO.save()

    return HttpResponse('Access Is Created')