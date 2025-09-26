from django.db import models

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
    image_url=models.URLField(blank=True)

#date field
    join_date=models.DateTimeField(auto_now=True)

    def __str__(self):
 #return string rep of model instance
        return f'{self.username}'