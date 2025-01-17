from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime
from .models import Contact, NewArrival, CartItem, WishlistItem
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def index(request):
    context = {"variable1": "i am great"}
    return render(request, 'index.html', context)

def men(request):
    return render(request, 'index.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('contact_number')
        desc = request.POST.get('message')
        contact_instance = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact_instance.save()
        messages.success(request, "Your message has been sent.")
    return render(request, 'contact.html')

def new_arrivals(request):
    products = NewArrival.objects.all().order_by('-created_at')
    return render(request, 'newarrival.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(NewArrival, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

def register_view(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('login')
        else:
            messages.error(request, 'Passwords do not match.')
    return render(request, 'register.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        remember_me = request.POST.get('remember_me', False)
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if remember_me:
                request.session.set_expiry(1209600)  # 2 weeks
            else:
                request.session.set_expiry(0)  # Session expires on browser close
            return redirect('index')  # Redirect to a home page or dashboard
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')

@login_required
def add_to_cart(request, pk):
    product = get_object_or_404(NewArrival, pk=pk)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

@login_required
def add_to_wishlist(request, pk):
    product = get_object_or_404(NewArrival, pk=pk)
    WishlistItem.objects.get_or_create(user=request.user, product=product)
    return redirect('wishlist')

@login_required
def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'cart.html', {'cart_items': cart_items})

@login_required
def wishlist_view(request):
    wishlist_items = WishlistItem.objects.filter(user=request.user)
    return render(request, 'wishlist.html', {'wishlist_items': wishlist_items})