from django.db import models
'''Name:Sarah Lam
Title:models.py
Purpose: the modesl for the Joke and Picture '''


# Create your models here.
'''The Joke class with the name of the contributer and the time stamps'''
class Joke(models.Model):
    text=models.TextField()
    create=models.DateTimeField(auto_now_add=True)
    con=models.CharField(max_length=100)

    '''the string '''
    def __str__(self):
        return self.text


'''The Picture class for storing the image_url and the image, name of contributr and time stamp of when created '''
class Picture(models.Model):
    con=models.CharField(max_length=100)
    image=models.URLField()
    create=models.DateTimeField(auto_now_add=True)

    '''the string of picture model '''
    def __str__(self):
        return self.image


