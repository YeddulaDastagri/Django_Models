from django.shortcuts import render 
from django.http import HttpResponse 
from app.models import *

# Create your views here. 

def insert_topic(request):
    tn=input("enter topicname") 
    tod=Topic.objects.get_or_create(topicname=tn) 
    if tod[1]:
        return HttpResponse("new topic is created") 
    else:
        return HttpResponse("given topic is already present")    


def insert_webpage(request):
    tn=input() 
    n=input() 
    url=input() 
    email=input() 
    LTO=Topic.objects.filter(topicname=tn)  
    if LTO:
        WTOD=WebPages.objects.get_or_create(topicname=LTO[0],name=n,urls=url,email=email)  
        if WTOD[1]:
            return HttpResponse("webpage is created") 
        else:
            return HttpResponse("wedpage is persent") 
    else:
        return HttpResponse("given topic is not present in database")    


def insert_access(request):  
    pk=int(input('enter of webpage')) 
    author=input('enter author') 
    date=input('enter date')  
    LWO=Webpages.objects.filter(pk=pk) 
    if LWO:
        ATOD=AccessRecords.objects.get_or_create(name=LWO[0],author=author,date=date) 
        if ATOD[1]:
            return HttpResponse('new access is created') 
        else:
            return HttpResponse('Given acess is present') 
    else:
        return HttpResponse('given parent webpage  table data is not present in database')      


