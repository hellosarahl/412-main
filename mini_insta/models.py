from django.db import models

# Create your models here.
class Profile(models.Model):
#define the data attributes of profile
#username, display_name, profile_image_url,bio_text, join_data
    username=models.TextField(blank=True)
    display_name=models.TextField(blank=True)
    profile_image_url=models.TextField(blank=True)
    bio_text=models.TextField(blank=True)
    image_url=models.URLField(blank=True)

#date field
    join_date=models.DateTimeField(auto_now=True)

    def __str__(self):
 #return string rep of model instance
        return f'{self.username}'