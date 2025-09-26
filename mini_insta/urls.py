#url patterns mini_insta/urls.py 

from django.urls import path
from .views import  ProfileListView, RandomProfileView, ProfileDetailView
#URL patterns are defined

app_name= "mini_insta"
urlpatterns=[
    """random profile on main"""
    path('',RandomProfileView.as_view(),name="random"),
    """show all profiles"""
    path('show_all/',ProfileListView.as_view(), name="show_all_profiles"),
    """show one profile"""
    path('profile/<int:pk>/',ProfileDetailView.as_view(), name='profile')

]