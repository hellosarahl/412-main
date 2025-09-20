#two python list in gloabl scope
#list of quotes strins
#list of images
from django.shortcuts import render 
from django.http import HttpRequest, HttpResponse
import random
#views 
#quotes 

#quotes
quotes= ["People throw rocks at things that shine",
         "Trash takes itself out every single time",
         "Just be yourself, there is no one better"
]
#images
images=[
" https://imageio.forbes.com/specials-images/imageserve/646e6affb9a2a85595a62c39/0x0.jpg?format=jpg&crop=1573,1574,x239,y256,safe&height=416&width=416&fit=bounds",
 "https://hips.hearstapps.com/hmg-prod/images/taylor-swift-performs-onstage-during-taylor-swift-the-news-photo-1733447389.jpg?resize=1200:*",
 "https://media.cnn.com/api/v1/images/stellar/prod/gettyimages-2162457025-20240916235044346.jpg?c=16x9&q=h_653,w_1160,c_fill/f_avif"
]

def quote(request):
    "For quote and image"
    context={
        "quote":random.choice(quotes),
        "image":random.choice(images),
        "title":"Quotes of the day"
    }
    return render(request, "quotes/quote.html", context)


def show_all(request):
    context={'quotes':quotes, 'images':images}
    return render(request, "quotes/show_all.html",context)


def about(request):
    "info of person"
    context={
       "info": "Taylor Swift is a singer known for her music and has won many Grammy awarrds." 
        
    }
    return render(request,"quotes/about.html",context)





