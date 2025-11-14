from django.contrib import admin

'''Name:Sarah Lam
Description: register for the admin for dad jokes
File:urls.py'''

# Register your models here.

from django.contrib import admin
from .models import Joke, Picture 

#register admin
admin.site.register(Joke)


#register the picture
admin.site.register(Picture)
