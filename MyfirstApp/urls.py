from django.contrib import admin
from django.urls import path
from MyfirstApp import views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',views.nav, name='nav'),
    path('home', views.Home, name='home'),
    path('ourclient', views.Ourclient, name='ourclient'),
    path('about', views.About, name='about'),
    path('team', views.Team, name='team'),
    path('contact', views.Cont, name='contact'),
    path('award', views.Award, name='award'),
    path('gallery', views.Gallery, name='gallery'),



    path('service', views.service, name='service'),
    path('radio', views.Radio, name='radio'),
    path('printmedia', views.PrintMedia, name='printmedia'),
    path('metro', views.Metro, name='metro'),

    path('pvr', views.Pvr, name='pvr'),
    path('airport', views.Airport, name='airport'),
    path('outdoor', views.Outdoor, name='outdoor'),
    path('car', views.Car, name='car'),
    path('socialmedia',views.SocialMedia, name='socialmedia'),
    path('mallbranding', views.MallBranding, name='mallbranding'),
    path('ipl', views.IPL, name='ipl'),
    path('bartermedia', views.BarterMedia, name='bartermedia'),
    path('tv', views.TV, name='tv')
    
    
]