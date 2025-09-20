from django.shortcuts import render
import random
import time
from datetime import datetime,timedelta
from django.http import HttpResponse
# Create your views here.
def order(request):
    template_name='restaurant/order.html'
    return render(request, template_name)


def confirmation(request):
    template_name='restaurant/confirmation.html'
    return render(request, template_name)

     
    


def main(request):
    images=["https://i5.walmartimages.com/seo/Selfie-Stick-Portable-Mini-Condenser-Microphone-With-3-5mm-Aux-Connector-Silver_a08a0806-e425-4ba0-8e3e-4214062d49ff.50dcbf1fbea07056d25c98450cc0f24c.jpeg"]
    context={
    "image":random.choice(images),
     }
    return render(request, "restaurant/main.html", context)

def submit(request):
    template_name="restaurant/confirmation.html"



    t=time.time()

    ran=random.randint(30,60)*60

    r=t+ran
    ready= time.ctime(r)

    menu= {"Mic's hot chicken tenders": 12.00, "Mic's hot cauliflower":7.99, "Mic's hot Chicken sliders":7.99, 
    "Mic's loaded fries": 7.99, "Hot chili": 2.99, "100% Nuclear Wassabi":2.99}
   
 
    
    if request.method=='POST':
        m=request.POST.getlist("menuitem")
        special=request.POST.getlist('special')
        option=request.POST.getlist('option')
        all=m+special+option
        total= sum(menu.get(item,0) for item in all)

        context={
        'name':request.POST.get('name',''),
        'phone':request.POST.get('phone',''),
        'email':request.POST.get('email',''),
        'instruct':request.POST.get('instruct',''),
        'ready':ready,
        'total':total,
        'menuitems':m,
        'special':special,
        'option':option,
      
        }

        return render(request, template_name, context)
    

    