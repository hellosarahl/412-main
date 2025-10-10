#url patterns mini_insta/urls.py 

"""urls.py that is for the mini_insta"""

from django.urls import path
from .views import * #ProfileListView, RandomProfileView, ProfileDetailView
#URL patterns are defined

app_name= "mini_insta"
urlpatterns=[
    #random profile view
    path('',RandomProfileView.as_view(),name="random"),
#show all profiles
    path('show_all/',ProfileListView.as_view(), name="show_all_profiles"),
    #show one profile
    path('profile/<int:pk>/',ProfileDetailView.as_view(), name='profile'),
    path('profile/create', CreateProfileView.as_view(), name='create_profile'),
   # path('profile/<int:pk>/create_comment',CreateCommentView.as_view(), name="create_comment"),

#shows one post through primary key
    path('post/<int:pk>/',PostDetailView.as_view(), name='post_detail'),
    #new post created by the profile
    path('profile/<int:pk>/create_post',CreatePostView.as_view(), name='create_post'),
    path('profile/<int:pk>/update',UpdateProfileView.as_view(),name='update_profile'),
    path('post/<int:pk>/delete',DeletePostView.as_view(), name='delete_post'),
   path('post/<int:pk>/update',UpdatePostView.as_view(),name='update_post'),
]

