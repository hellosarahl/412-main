'''Name:Sarah Lam 
Description:the urls for the five photos
File:urls.py
'''

from django.urls import path 
from .import views

urlpatterns=[
    #shows a joke and a photo
    path('',views.home,name='home'),
    path('random/',views.home,name='random'),
    path('jokes/',views.jokes, name='jokes'),
    path('joke/<int:pk>/',views.jokes_one, name='jokes_one'),

    path('pictures/',views.allpicture, name='allpicture'),

    path('picture/<int:pk>/',views.picture, name='picture'),



    #api urls 
    path('api/',views.RandomJoke.as_view()),
    path('api/random',views.RandomJoke.as_view()),
    path('api/jokes',views.JokeCreateView.as_view()),
    path('api/joke/<int:pk>',views.JokeDetail.as_view()),
    path('api/pictures',views.PicList.as_view()),
    path('api/picture/<int:pk>',views.PicDetail.as_view()),
    path('api/random_picture',views.RandomPic.as_view()),


]