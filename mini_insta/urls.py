#url patterns mini_insta/urls.py 

from django.urls import path
from .views import * #ProfileListView, RandomProfileView, ProfileDetailView
#URL patterns are defined

app_name= "mini_insta"
urlpatterns=[
    path('',RandomProfileView.as_view(),name="random"),
#show all profiles
    path('show_all/',ProfileListView.as_view(), name="show_all_profiles"),
    #show one profile
    path('profile/<int:pk>/',ProfileDetailView.as_view(), name='profile'),
    path('profile/create', CreateProfileView.as_view(), name='create_profile'),
   # path('profile/<int:pk>/create_comment',CreateCommentView.as_view(), name="create_comment"),

    path('post/<int:pk>/',PostDetailView.as_view(), name='post_detail'),
    path('profile/<int:pk>/create_post',CreatePostView.as_view(), name='create_post'),
]

