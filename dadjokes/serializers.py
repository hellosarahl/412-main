'''Name:Sarah Lam
Description: Serializer for each model Picture and Joke
'''
from rest_framework import serializers
from .models import Joke,Picture 

'''Serializer class for the model joke'''
class JokeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Joke
        fields='__all__'

class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model=Picture
        fields='__all__'


