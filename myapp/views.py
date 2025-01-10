# admin id admin pw admin

from django.shortcuts import render,HttpResponse
from datetime import datetime
from myapp.models import Contact
from django.contrib import messages 

# Create your views here
def index(request):
    context={
        "variable1" : "i am great",
        }
    messages.success(request,'This is a test message')
    return render(request,'index.html',context)
 
  
        

    messages.success(request,'This message has been sent')
    return(request,'index.html')
    
    
    
    
def index(request):
    return render(request,'index.html')

# def index(request):
#     return render(request,'base.html')

def men(request):
    return render(request,'index.html')

def women (request):
    return render(request,'index.html')
def contact(request):
    if request.method == "POST":  # Make sure it's POST method
        # Accessing POST data correctly (use request.POST instead of request.post)
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('contact_number')  # Use 'contact_number' instead of 'phone' as per your form
        desc = request.POST.get('message')  # Use 'message' instead of 'desc' based on your form

        # Create a new instance of the Contact model
        contact_instance = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())

        # Save the instance to the database
        contact_instance.save()

        # Display success message
        messages.success(request, "Your message has been sent.")





    # Render the contact page again
    return render(request, 'contact.html')
    # return render(request,'contact.html')
def newarrival(request):
    return render(request,'newarrival.html')
def womennewarrival(request):
    return(request,'womennewarrival.html') 




from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def detail(request, image_id):
    # Example data, replace with actual data retrieval
    images = {
        1: {'url': '/static/menarrival1.png', 'title': 'Signature track pant', 'description': 'This is a stylish and comfortable track pant designed to provide the perfect balance of ease and durability.'},
        2: {'url': '/static/menarrival2.png', 'title': 'Ease and Elevate track pant', 'description': 'This track pant is perfect for both athletic performance and casual wear. Designed for maximum comfort and ease.'},
        3: {'url': '/static/menarrival3.png', 'title': 'Track Shoot', 'description': 'This product is designed for high-intensity activities with a focus on performance and comfort.'},
    }
    image = images.get(image_id, None)
    if image:
        return render(request, 'detail.html', {
            'image_url': image['url'],
            'image_title': image['title'],
            'image_description': image['description'],
        })
    else:
        # Handle image not found
        return render(request, '404.html', status=404)  
    
    
    
# men-newarrival
def newarrival(request):
    return render(request, 'newarrival.html')

