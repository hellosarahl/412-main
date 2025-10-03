
#mini_insta/form.py
#forms for creatte, update, delete operation 
from django import forms
from .models import *
from .models import Profile

class CreateProfileForm(forms.ModelForm):
    ''' A form to add to article to the database'''
    class Meta:
        '''associate form with model of data base'''
        model=Profile
        fields=['username','display_name','profile_image_url','bio_text','image_url']


class CreatePostForm(forms.ModelForm):

    class Meta:
        model=Post
        fields= ['caption']