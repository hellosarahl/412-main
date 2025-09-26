from django.contrib import admin

# Register profile model 
from .models import Profile


"""register so can be in django admin"""
admin.site.register(Profile)
