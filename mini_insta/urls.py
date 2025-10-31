#url patterns mini_insta/urls.py 

"""urls.py that is for the mini_insta"""

from django.urls import path
from .views import * #ProfileListView, RandomProfileView, ProfileDetailView
#URL patterns are defined
from .views import ShowFollowerDetailView,ShowFollowingDetailView,PostFeedListView
# generic views for authentication .authorization 
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

app_name= "mini_insta"
urlpatterns=[
    #random profile view
    path('',RandomProfileView.as_view(),name="random"),
#show all profiles
    path('show_all/',ProfileListView.as_view(), name="show_all_profiles"),
    #show one profile
    path('profile/',ProfileDetailView.as_view(), name='profile'),
    path('profile/create', CreateProfileView.as_view(), name='create_profile'),
   # path('profile/<int:pk>/create_comment',CreateCommentView.as_view(), name="create_comment"),

#shows one post through primary key
    path('post/<int:pk>/',PostDetailView.as_view(), name='post_detail'),
    #new post created by the profile
    path('profile/create_post',CreatePostView.as_view(), name='create_post'),
    path('profile/update',UpdateProfileView.as_view(),name='update_profile'),
    path('post/<int:pk>/delete',DeletePostView.as_view(), name='delete_post'),
   path('post/<int:pk>/update',UpdatePostView.as_view(),name='update_post'),

   #path for following and followers
   path('profile/followers',ShowFollowerDetailView.as_view(),name='show_followers'),
   path('profile/following',ShowFollowingDetailView.as_view(),name='show_following'),
   path('profile/feed',PostFeedListView.as_view(),name='profile_feed'),
   path('profile/search',SearchView.as_view(),name='search'),
   
   #authentication views 
   path('login/',auth_views.LoginView.as_view(template_name='mini_insta/login.html'),name='login'),
   path('logout/',auth_views.LogoutView.as_view(template_name='mini_insta/logout.html'),name='logout'),
   path('register/',UserRegistrationView.as_view(),name='register'),
   path('profile/create',CreateProfileView.as_view(), name='create_profile')

]

