from django.contrib import admin
from MyfirstApp.models import Contact
# from .models import Profile, Post, LikePost, FollowersCount
#from MyfirstApp.models import *

# Register your models here.

# Admin panel ke header, title, aur index text ko change karna
admin.site.site_header = "Pooja Movie Creations Admin Panel"
admin.site.site_title = "Pooja Movie Creations Admin"
admin.site.index_title = "Welcome to Pooja Movie Creations Dashboard"


admin.site.register(Contact)

# admin.site.register(Profile)
# admin.site.register(Post)
# admin.site.register(LikePost)
# admin.site.register(FollowersCount)