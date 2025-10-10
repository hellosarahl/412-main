
#mini_insta/form.py
#forms for create, update, delete operation 
from django import forms
from .models import *
from .models import Profile

#create profile form which is for creating a new profile
class CreateProfileForm(forms.ModelForm):
    ''' A form to add profile to the database'''
    class Meta:
        '''associate form with model of data base'''
        model=Profile
       # fields=['username','display_name','profile_image_url','bio_text','image_url']
       #now displaying image_file so changed to that
        fields=['username','display_name','profile_image_url','bio_text','image_file']


class UpdateProfileForm(forms.ModelForm):
    '''A form to handle an update to a Profile'''
    class Meta:
        '''associate this form with a model in our database'''
        model=Profile
        fields=['display_name','username']


class CreatePostForm(forms.ModelForm):
    """form for creating a new post in mini insta"""
    class Meta:
        """purpose to define fields to display"""
        model=Post
        fields= ['caption']