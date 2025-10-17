
"""models.py for mini_insta App
this app has the profile,post and photo models"""

"""
File:models.py
    Author:Sarah Lam 
Methods used to get data and url
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
    
     #return list of profiles who follow this profile
    def get_followers(self):
        f=Follow.objects.filter(profile=self)
        li=[]
        for follow in f:
            li+=[follow.follower_profile]
        return li
    
    #get the number of follows
    def get_num_followers(self):
        return Follow.objects.filter(profile=self).count()
    
    #get the number of followers
    def get_following(self):
        f=Follow.objects.filter(follower_profile=self)
        li=[]
        for follow in f:
            li+=[follow.profile]
        return li
    
    #return count of how many profiles ar ebeing followed
    def get_num_following(self):
        return Follow.objects.filter(follower_profile=self).count()
    
  


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
    
    def get_all_comments(self):
        """gets all the comments"""
        return self.comments.all().order_by('timestamp')
    def get_likes(self):
        """gets all like object"""
        return self.likes.all()
    



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
        """return the url of the image"""
        if self.image_url:
            return self.image_url
        elif self.image_file:
            return self.image_file.url
        return ''
    
"""connects idea of two nodes within the social network"""
class Follow(models.Model):
    #the profile followed-publisher
    profile=models.ForeignKey('Profile',on_delete=models.CASCADE,related_name='followers')
    #profile for subscribers
    follower_profile=models.ForeignKey('Profile',on_delete=models.CASCADE,related_name='following')
    #timestamp of when follower began
    timestamp=models.DateTimeField(auto_now_add=True)

    #view follow relationship as a string rep
    def __str__(self):
           """returns the string rep of follow"""
           return f' {self.follower_profile} follows {self.profile}'
    
   
        
"""data model representing a comment """
class Comment(models.Model):
    #fk for post this comment
      post=models.ForeignKey('Post',on_delete=models.CASCADE,related_name='comments')
      #fk for profile that made comment
      profile=models.ForeignKey('Profile',on_delete=models.CASCADE,related_name='comments')
    #timestamp for comments
      timestamp=models.DateTimeField(auto_now_add=True)
      #text of comment
      t=models.TextField()

      def __str__(self):
          #displays the comment
          return f'Comment {self.profile} in {self.post} during {self.timestamp}'
      

"""data model representing a like """
class Like(models.Model):
    #fk for post this like relates to 
      post=models.ForeignKey('Post',on_delete=models.CASCADE,related_name='likes')
      #fk for profile that is making this like
      profile=models.ForeignKey('Profile',on_delete=models.CASCADE,related_name='likes')
    #timestamp for when like was created
      timestamp=models.DateTimeField(auto_now_add=True)
      def __str__(self):
          #displays the like
          return f'Like {self.profile} in {self.post} during {self.timestamp}'
    




  
        