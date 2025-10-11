"""
URL configuration for cs412_project_temp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static 
from django.views.generic import RedirectView
from django.conf import settings

"""URL pattern for proj"""
urlpatterns = [
    path('admin/', admin.site.urls),

   # path('',include('restaurant.urls')),

   path('mini_insta/',include('mini_insta.urls')),
   path('',RedirectView.as_view(url='/mini_insta/',permanent=False)),
 
]
#static files for development
urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

