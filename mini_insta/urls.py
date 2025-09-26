#url patterns mini_insta/urls.py 

from django.urls import path
from .views import  ProfileListView, RandomProfileView, ProfileDetailView

urlpatterns=[
    path('',RandomProfileView.as_view(),name="random"),
    path('show_all',ProfileListView.as_view(), name="show_all"),
    path('profile/<int:pk>/',ProfileDetailView.as_view(), name='profile')

]