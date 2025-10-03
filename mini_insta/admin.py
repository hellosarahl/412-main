from django.contrib import admin

# Register profile model 
from .models import Profile
from .models import Photo
from .models import Post

"""register so can be in django admin"""
admin.site.register(Profile)
admin.site.register(Photo)
admin.site.register(Post)