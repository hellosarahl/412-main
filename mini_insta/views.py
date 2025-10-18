
"""views.py for the mini insta app
this is for displaying and creating the profiles and post

"""



from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Profile,Post,Photo,Post
import random
from .forms import CreateProfileForm, CreatePostForm, UpdateProfileForm
from django.conf import settings
from django.urls import reverse
from django.db.models import Q

# Class based views for Mini Insta
#display all profiles
class ProfileListView(ListView):
    """list view that is for displaying all profiles"""
    model=Profile
    template_name= "mini_insta/show_all_profiles.html"
    """for accessing profile """
    context_object_name= "profiles"

# for displaying the profile based on key
class ProfileDetailView(DetailView):
    model=Profile
    template_name="mini_insta/show_profile.html"
    """access profile"""
    context_object_name="profile"

#to display random profile
class RandomProfileView(DetailView):
    model=Profile
    template_name="mini_insta/show_profile.html"
    context_object_name="profile"


    """return random profile at random"""

    def get_object(self):
        all_profiles=Profile.objects.all()
        """one at a time selected"""
        profile=random.choice(all_profiles)
        return profile



#define sublass of create view to handle creations of profile object
class CreateProfileView(CreateView):
 """View for handling new profile"""
 model=Profile
 form_class= CreateProfileForm
 template_name="mini_insta/create_profile_form.html"

 def form_valid(self,form):
    '''override deafault method to add debug info '''
    #print out form data
    print(f'CreateProfileView.form_valid():{form.cleaned_data}')

    #delegate work to superclass to do the rest 
    return super().form_valid(form)

 
 def get_success_url(self):
   '''redict url to redirect to after creating new post'''   
   #pk=self.kwargs['pk']
   #call reverse to generate url 
   return reverse('mini_insta:profile',kwargs={'pk':self.object.pk})
 


class PostDetailView(DetailView):
    """display single post and all photos"""
    model=Post
    template_name="mini_insta/show_post.html"
    context_object_name="post"


class CreatePostView(CreateView):
   """handles the creation of a newly created post"""
   model=Post 
   form_class=CreatePostForm
   template_name="mini_insta/create_post_form.html"

   def form_valid(self,form):
      """creates photo when there is img url"""
      pk=self.kwargs['pk']
      profile=Profile.objects.get(pk=pk)
   #attach article to comment
      form.instance.profile=profile
      r= super().form_valid(form)
      images=self.request.FILES.getlist('images')
      for image in images:
         Photo.objects.create(post=self.object,image_file=image)
      return r
     
   
   def get_success_url(self): 
      """goes to profile page after creation of post"""
      return reverse('mini_insta:profile',kwargs={'pk':self.object.profile.pk})
   
   def get_context_data(self,**kwargs):
      """profile object is added so template has access"""
      context=super().get_context_data(**kwargs)
      p=self.kwargs['pk']
      context['profile']=Profile.objects.get(pk=p)
      return context

class UpdateProfileView(UpdateView):
   '''view class to ahandle update of an profile based on its pk'''
   model=Profile
   form_class=UpdateProfileForm
   template_name="mini_insta/update_profile_form.html"

   


class DeletePostView(DeleteView):
   '''view class to delete a post on a profile'''
   model=Post
   template_name="mini_insta/delete_post_form.html"

   def get_success_url(self):
      '''return the url to redirect to after a successful delete'''
      # find pk for this post:
      pk=self.kwargs['pk']
      # find the post object
      post=Post.objects.get(pk=pk)
      # find the pk of profile to which this post is associated
      profile=post.profile
      return reverse('mini_insta:profile',kwargs={'pk':profile.pk})

   
   def get_context_data(self, **kwargs):
      c=super().get_context_data(**kwargs)
      post=self.get_object()
      c['post']=post
      c['profile']=post.profile
      return c



class UpdatePostView(UpdateView):
   model=Post
   fields=['caption']
   template_name="mini_insta/update_post_form.html"

   def get_success_url(self):
      return reverse('mini_insta:post_detail', kwargs={'pk':self.object.pk})

"""shows the follower details"""
class ShowFollowerDetailView(DetailView):
   model=Profile
   #template for the follower data
   template_name="mini_insta/show_followers.html"
   context_object_name='profile'

   """add context daya so template displays followers"""
   def get_context_data(self, **kwargs):
       con=super().get_context_data(**kwargs)
       p=self.kwargs['pk']
       profile=self.get_object()
       con['following_list']=profile.get_followers()
       return con


"""shows the follow detail"""
class ShowFollowingDetailView(DetailView):
   model=Profile
   #template for the following data
   template_name="mini_insta/show_following.html"
   context_object_name='profile'

   """add context daya so template displays following"""
   def get_context_data(self, **kwargs):
       con=super().get_context_data(**kwargs)
       p=self.kwargs['pk']
       profile=self.get_object()
       con['following_list']=profile.get_following()
       return con




"""view class associated with show feed """

class PostFeedListView(ListView):
    model=Post
    template_name="mini_insta/show_feed.html"

    """gets the post that belong to profile by pk from url """
    def get_queryset(self):
       p=self.kwargs['pk']
       pro=Profile.objects.get(pk=p)
       return Post.objects.filter(profile=pro)
    
    """add context daya so template displays profile """
    def get_context_data(self, **kwargs):
       con=super().get_context_data(**kwargs)
       p=self.kwargs['pk']
       con['profile']=Profile.objects.get(pk=p)
       return con
    """search for profiles and post"""
class SearchView(ListView):
    template_name="mini_insta/search_results.html"

    def get_context_data(self, **kwargs):
       con=super().get_context_data(**kwargs)
       #find if query is present
       search=self.request.GET.get('m','')
       con['query']=search

       #search for match in the profiles
       con['profiles']=Profile.objects.filter( Q(bio_text__icontains=search)|Q(username__icontains=search)|Q(display_name__icontains=search)
       )
    

       #profile object we use for resarch 
       profile=None
       if self.request.user.is_authenticated:
          profile=Profile.objects.filter(username=self.request.user).first()
       else:
          profile=None
       con['profile']=profile

       #post that matches the query
       con['post']=self.get_queryset()

       return con
    

    
    """handles any request"""
    def dispatch(self,request,*args,**kwargs):
      q=request.GET.get('m')

      #user login get info
      if not q:
            profile=Profile.objects.filter(pk=self.kwargs.get('pk')).first()
          #show the profile info 
            return render(request, 'mini_insta/search.html',{'profile':profile})
       
       #continue normal search,return superclass version

      return super().dispatch(request,*args,**kwargs)
    
    """method used to obtain the query set"""
    def get_queryset(self):
       q=self.request.GET.get('m')
       if not q:
          return Post.objects.none()
       else:
          return Post.objects.filter(caption__icontains=q)
       
    
    """the form from the search"""
#def form(request,pk):
       #return render(request,'mini_insta/search.html',{'profile_pk':pk})

    









#def form_valid(self,form):
   # print (form.cleaned_data)