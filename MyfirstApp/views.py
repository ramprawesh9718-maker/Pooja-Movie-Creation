from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect
# from django.contrib.auth.models import User, auth
from datetime import datetime
from MyfirstApp.models import Contact


# Create your views here.

def nav(request):
    return render(request,"nav.html")

def Home(request):
    return render(request,"home.html")

def Ourclient(request):
    return render(request,"Ourclient.html")

def About(request):
    return render(request,"about.html")
    
def Team(request):
    return render(request,"OurMission.html")

def Cont(request):
    success = False
    if request.method == "POST":
        name=request.POST.get('name')
        contact=request.POST.get('contact')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        detail=Contact(name=name, contact=contact, email=email, subject=subject, message=message, date=datetime.today())
        detail.save()
        success = True
    return render(request,"contact.html", {"success": success})

def Award(request):
    return render(request,"Award.html")

def Gallery(request):
    return render(request,"gallery.html")





def service(request):
    return render(request,"service.html")
def Radio(request):
    return render(request,"radio.html")
def PrintMedia(request):
    return render(request,"printmedia.html")
def Metro(request):
    return render(request,"metro.html")
def Airport(request):
    return render(request,"airport.html")
def Pvr(request):
    return render(request,"pvr.html")
def Outdoor(request):
    return render(request,"outdoor.html")
def Car(request):
    return render(request,"car.html")
def SocialMedia(request):
    return render(request,"socialmedia.html")
def MallBranding(request):
    return render(request,"mall.html")
def IPL(request):
    return render(request,"ipl.html")
def BarterMedia(request):
    return render(request,"barter.html")
def TV(request):
    return render(request,"tv.html")


