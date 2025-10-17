from django.contrib import admin


# Register profile model 
from .models import Profile
from .models import Photo
from .models import Post
from .models import Follow
from .models import Comment
from .models import Like
"""register so can be in django admin"""
admin.site.register(Profile)
admin.site.register(Photo)
admin.site.register(Post)
"""register follow in django"""
admin.site.register(Follow)
"""register comment"""
admin.site.register(Comment)
"""register like"""
admin.site.register(Like)