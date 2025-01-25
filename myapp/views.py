from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime
from .models import Contact, CartItem, WishlistItem, MenNewArrival, MenAutumnWinter, WomenNewArrival, WomenAutumnWinter, KidsNewArrival, KidsAutumnWinter
from .models import (MenTShirts, MenPolos, MenShorts, MenTrackpantsJoggers, 
                     MenRunning, MenYoga, WomenTShirts, WomenPolos, WomenShorts,
                     WomenTrackpantsJoggers, WomenRunning, WomenYoga, KidsTShirts,
                     KidsPolos, KidsShorts, KidsTrackpantsJoggers, KidsRunning, KidsYoga)
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

def index(request):
    return render(request, 'index.html')

def men(request):
    return render(request, 'index.html')

# Men Category Views
def men_new_arrivals(request):
    products = MenNewArrival.objects.all().order_by('-created_at')
    return render(request, 'men_newarrival.html', {'products': products})

def men_autumn_winter(request):
    products = MenAutumnWinter.objects.all()
    return render(request, 'men_autumn_winter.html', {'products': products})

def men_tshirts(request):
    products = MenTShirts.objects.all().order_by('-created_at')
    return render(request, 'men_tshirts.html', {'products': products})

def men_polos(request):
    products = MenPolos.objects.all().order_by('-created_at')
    return render(request, 'men_polos.html', {'products': products})

def men_shorts(request):
    products = MenShorts.objects.all().order_by('-created_at')
    return render(request, 'men_shorts.html', {'products': products})

def men_trackpants_joggers(request):
    products = MenTrackpantsJoggers.objects.all().order_by('-created_at')
    return render(request, 'men_trackpants_joggers.html', {'products': products})

def men_running(request):
    products = MenRunning.objects.all().order_by('-created_at')
    return render(request, 'men_running.html', {'products': products})

def men_yoga(request):
    products = MenYoga.objects.all().order_by('-created_at')
    return render(request, 'men_yoga.html', {'products': products})

# Women Category Views
def women_new_arrivals(request):
    products = WomenNewArrival.objects.all().order_by('-created_at')
    return render(request, 'women_newarrival.html', {'products': products})

def women_autumn_winter(request):
    products = WomenAutumnWinter.objects.all()
    return render(request, 'women_autumn_winter.html', {'products': products})

def women_tshirts(request):
    products = WomenTShirts.objects.all().order_by('-created_at')
    return render(request, 'women_tshirts.html', {'products': products})

def women_polos(request):
    products = WomenPolos.objects.all().order_by('-created_at')
    return render(request, 'women_polos.html', {'products': products})

def women_shorts(request):
    products = WomenShorts.objects.all().order_by('-created_at')
    return render(request, 'women_shorts.html', {'products': products})

def women_trackpants_joggers(request):
    products = WomenTrackpantsJoggers.objects.all().order_by('-created_at')
    return render(request, 'women_trackpants_joggers.html', {'products': products})

def women_running(request):
    products = WomenRunning.objects.all().order_by('-created_at')
    return render(request, 'women_running.html', {'products': products})

def women_yoga(request):
    products = WomenYoga.objects.all().order_by('-created_at')
    return render(request, 'women_yoga.html', {'products': products})

# Kids Category Views
def kids_new_arrivals(request):
    products = KidsNewArrival.objects.all().order_by('-created_at')
    return render(request, 'kids_newarrival.html', {'products': products})

def kids_autumn_winter(request):
    products = KidsAutumnWinter.objects.all().order_by('-created_at')
    return render(request, 'kids_autumn_winter.html', {'products': products})

def kids_tshirts(request):
    products = KidsTShirts.objects.all().order_by('-created_at')
    return render(request, 'kids_tshirts.html', {'products': products})

def kids_polos(request):
    products = KidsPolos.objects.all().order_by('-created_at')
    return render(request, 'kids_polos.html', {'products': products})

def kids_shorts(request):
    products = KidsShorts.objects.all().order_by('-created_at')
    return render(request, 'kids_shorts.html', {'products': products})

def kids_trackpants_joggers(request):
    products = KidsTrackpantsJoggers.objects.all().order_by('-created_at')
    return render(request, 'kids_trackpants_joggers.html', {'products': products})

def kids_running(request):
    products = KidsRunning.objects.all().order_by('-created_at')
    return render(request, 'kids_running.html', {'products': products})

def kids_yoga(request):
    products = KidsYoga.objects.all().order_by('-created_at')
    return render(request, 'kids_yoga.html', {'products': products})

def product_detail(request, category, pk):
    if category == 'men_newarrival':
        product = get_object_or_404(MenNewArrival, pk=pk)
    elif category == 'women_newarrival':
        product = get_object_or_404(WomenNewArrival, pk=pk)
    elif category == 'kids_newarrival':
        product = get_object_or_404(KidsNewArrival, pk=pk)
    elif category == 'men_tshirts':
        product = get_object_or_404(MenTShirts, pk=pk)
    elif category == 'men_polos':
        product = get_object_or_404(MenPolos, pk=pk)
    elif category == 'men_shorts':
        product = get_object_or_404(MenShorts, pk=pk)
    elif category == 'men_trackpants_joggers':
        product = get_object_or_404(MenTrackpantsJoggers, pk=pk)
    elif category == 'men_running':
        product = get_object_or_404(MenRunning, pk=pk)
    elif category == 'men_yoga':
        product = get_object_or_404(MenYoga, pk=pk)
    elif category == 'women_tshirts':
        product = get_object_or_404(WomenTShirts, pk=pk)
    elif category == 'women_polos':
        product = get_object_or_404(WomenPolos, pk=pk)
    elif category == 'women_shorts':
        product = get_object_or_404(WomenShorts, pk=pk)
    elif category == 'women_trackpants_joggers':
        product = get_object_or_404(WomenTrackpantsJoggers, pk=pk)
    elif category == 'women_running':
        product = get_object_or_404(WomenRunning, pk=pk)
    elif category == 'women_yoga':
        product = get_object_or_404(WomenYoga, pk=pk)
    elif category == 'kids_tshirts':
        product = get_object_or_404(KidsTShirts, pk=pk)
    elif category == 'kids_polos':
        product = get_object_or_404(KidsPolos, pk=pk)
    elif category == 'kids_shorts':
        product = get_object_or_404(KidsShorts, pk=pk)
    elif category == 'kids_trackpants_joggers':
        product = get_object_or_404(KidsTrackpantsJoggers, pk=pk)
    elif category == 'kids_running':
        product = get_object_or_404(KidsRunning, pk=pk)
    elif category == 'kids_yoga':
        product = get_object_or_404(KidsYoga, pk=pk)
    else:
        product = None
    return render(request, 'product_detail.html', {'product': product, 'category': category})


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
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirect to the home page or any other page
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')

@login_required
def add_to_cart(request, pk, category):
    if category == 'men':
        product = get_object_or_404(MenNewArrival, pk=pk)
    elif category == 'women':
        product = get_object_or_404(WomenNewArrival, pk=pk)
    elif category == 'kids':
        product = get_object_or_404(KidsNewArrival, pk=pk)
    else:
        product = None
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

@login_required
def add_to_wishlist(request, pk, category):
    if category == 'men':
        product = get_object_or_404(MenNewArrival, pk=pk)
    elif category == 'women':
        product = get_object_or_404(WomenNewArrival, pk=pk)
    elif category == 'kids':
        product = get_object_or_404(KidsNewArrival, pk=pk)
    else:
        product = None
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

@login_required
def profile(request):
    return render(request, 'profile.html')




from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful. You are now logged in.')
            return redirect('index')  # Redirect to the home page or any other page
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})