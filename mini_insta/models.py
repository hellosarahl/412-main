
"""models.py for mini_insta App
this app has the profile,post and photo models

"""



from django.db import models
from django .urls import reverse

# Profile model for the mini insta 
class Profile(models.Model):
#define the data attributes of profile
#username, display_name, profile_image_url,bio_text, join_data
#username of profile
    username=models.TextField(blank=True)
    """display name of the user"""
    display_name=models.TextField(blank=True)
    """url of profile image"""
    profile_image_url=models.TextField(blank=True)
    """user bio"""
    bio_text=models.TextField(blank=True)
    """image"""
   # image_url=models.URLField(blank=True)
   #an actual image 
    image_file=models.ImageField(blank=True)

#date field
    join_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
 #return string rep of model instance
        return f'{self.username}'
    
    def get_absolute_url(self):
        '''return url to display oen instance of each object'''
        return reverse('mini_insta:profile',kwargs={'pk':self.pk})
    
    def get_all_posts(self):
        '''return queryset of post'''
        post=Post.objects.filter(profile=self)
        return post
    
  


class Post(models.Model):
    """The Post that is made by the Profile of Mini insta
    """
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE)
    caption=models.TextField(blank=False)
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """returns the string rep of post"""
        return f'Post by {self.profile.username} at {self.timestamp}'
    
    def get_all_photos(self):
        
        '''return all photos associated with post'''
        return Photo.objects.filter(post=self)



class Photo(models.Model):
    '''Encapsulate idea of comment about profile'''
    #data attributes for comments
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    image_url=models.URLField(blank=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    image_file=models.ImageField(blank=True)
    
    def __str__(self):
        '''return string rep of this comment'''
        if self.image_file:
            return f'Photo of post {self.post.id} at {self.timestamp} (file)'
        elif self.image_url:
              return f'Photo of post {self.post.id} at {self.timestamp} (url)'
        else:
               return f'Photo of post {self.post.id} at {self.timestamp}(no image)'



    def get_image_url(self):
        if self.image_url:
            return self.image_url
        elif self.image_file:
            return self.image_file.url
        return ''

  
        