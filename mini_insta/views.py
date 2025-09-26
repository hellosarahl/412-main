from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Profile
import random

# Class based views for Mini Insta
class ProfileListView(ListView):
    model=Profile
    template_name= "mini_insta/show_all_profiles.html"
    """for accessing profile """
    context_object_name= "profiles"

# for displaying the profile based on key
class ProfileDetailView(DetailView):
    model=Profile
    template_name="mini_insta/show_profile.html"
    """access profile"""
    context_object_name="profile"

#to display random profile
class RandomProfileView(DetailView):
    model=Profile
    template_name="mini_insta/show_profile.html"
    context_object_name="profile"


    """return random profile at random"""

    def get_object(self):
        all_profiles=Profile.objects.all()
        """one at a time selected"""
        profile=random.choice(all_profiles)
        return profile






