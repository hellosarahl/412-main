#voter_analytics/urls.py
'''Name:Sarah Lam
File:urls.py
Description: The urls of the project
'''
from django.urls import path
from . import views
from .views import VoterListView,VoterDetailView
from .views import GraphsView

urlpatterns=[
    #map the url(empty string to the views)
    path(r'', views.VoterListView.as_view(), name='voters'),
    path('results/',views.VoterListView.as_view(), name='voter_list'),
    path('voter/<int:pk>',VoterDetailView.as_view(),name="voter"),
    path('graphs/',GraphsView.as_view(), name="graphs"),
    

        
]

