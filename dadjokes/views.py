'''Name:Sarah Lam
Description:the views for the picture and jokes
File:urls.py '''



from django.shortcuts import render
from .models import Joke, Picture
import random
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import JokeSerializer,PictureSerializer




# Create your views here.
'''home for the random joke and the photo'''
def home(request):
    joke=random.choice(Joke.objects.all())
    pic=random.choice(Picture.objects.all())
    return render(request, 'home.html',{'joke':joke,'pic':pic})


'''the joke page '''
def jokes(request):
    jokes=Joke.objects.all()
    return render(request, 'joke.html',{'jokes':jokes})


'''show one joke by the pk '''
def jokes_one(request,pk):
    jokes=Joke.objects.all()
    picked=None
    for i in jokes:
        if i.pk==pk:
            picked=i
            break
    return render(request, 'joke_one.html', {'joke':picked})


'''page that has all photos'''

def allpicture(request):
    all=Picture.objects.all()
    return render(request, 'picture.html',{'pictures':all})


'''show one pic by pk'''
def picture(request,pk):
    all=Picture.objects.all()
    pick=None 
    for p in all:
        if p.pk==pk:
            pick=p
            break
    return render(request, 'picture_pj.html',{'picture':pick})


# api views

class RandomJoke(APIView):
    def get(self,request):
        j=random.choice(Joke.objects.all())
        return Response(JokeSerializer(j).data)
    

# rand pic

class RandomPic(APIView):
    def get(self,request):
        p=random.choice(Picture.objects.all())
        return Response(PictureSerializer(p).data)
    

#list all of them
class JokeCreateView(generics.ListCreateAPIView):
    queryset= Joke.objects.all()
    serializer_class=JokeSerializer

#pk joeks
class JokeDetail(generics.RetrieveAPIView):
    queryset=Joke.objects.all()
    serializer_class=JokeSerializer

class PicList(generics.ListAPIView):
    queryset=Picture.objects.all()
    serializer_class=PictureSerializer 

class PicDetail(generics.RetrieveAPIView):
    queryset=Picture.objects.all()
    serializer_class=PictureSerializer 







                  