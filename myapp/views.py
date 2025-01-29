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
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Product, Order
from .models import CartItem, Product, Order, BillingInfo 

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact_number = request.POST.get('contact_number')
        message = request.POST.get('message')
        
        # Create and save the Contact object
        contact = Contact(name=name, email=email, contact_number=contact_number, message=message)
        contact.save()
        
        # Add a success message
        messages.success(request, 'Your message has been sent successfully!')
        
        # Redirect to the same page after form submission
        return redirect('contact')  # Changed from 'contact_us' to 'contact'
    
    return render(request, 'contact.html')

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
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful. You are now logged in.')
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')

@login_required
def add_to_cart(request, category, pk):
    product_model = None
    if category == 'men_newarrival':
        product_model = MenNewArrival
    elif category == 'women_newarrival':
        product_model = WomenNewArrival
    elif category == 'kids_newarrival':
        product_model = KidsNewArrival
    elif category == 'men_tshirts':
        product_model = MenTShirts
    elif category == 'men_polos':
        product_model = MenPolos
    elif category == 'men_shorts':
        product_model = MenShorts
    elif category == 'men_trackpants_joggers':
        product_model = MenTrackpantsJoggers
    elif category == 'men_running':
        product_model = MenRunning
    elif category == 'men_yoga':
        product_model = MenYoga
    elif category == 'women_tshirts':
        product_model = WomenTShirts
    elif category == 'women_polos':
        product_model = WomenPolos
    elif category == 'women_shorts':
        product_model = WomenShorts
    elif category == 'women_trackpants_joggers':
        product_model = WomenTrackpantsJoggers
    elif category == 'women_running':
        product_model = WomenRunning
    elif category == 'women_yoga':
        product_model = WomenYoga
    elif category == 'kids_tshirts':
        product_model = KidsTShirts
    elif category == 'kids_polos':
        product_model = KidsPolos
    elif category == 'kids_shorts':
        product_model = KidsShorts
    elif category == 'kids_trackpants_joggers':
        product_model = KidsTrackpantsJoggers
    elif category == 'kids_running':
        product_model = KidsRunning
    elif category == 'kids_yoga':
        product_model = KidsYoga

    specific_product = get_object_or_404(product_model, pk=pk)
    
    # Create or get the Product instance
    product, created = Product.objects.get_or_create(
        title=specific_product.title,
        description=specific_product.description,
        price=specific_product.price,
        category=category,
        image=specific_product.image
    )

    quantity = int(request.POST.get('quantity', 1))

    if product.quantity >= quantity:
        cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
        if created:
            cart_item.quantity = quantity
        else:
            cart_item.quantity += quantity
        cart_item.save()
        product.quantity -= quantity
        product.save()
        messages.success(request, 'Product added to cart.')
    else:
        messages.error(request, 'Not enough stock available.')

    return redirect('cart')

@login_required
def add_to_wishlist(request, category, pk):
    product_model = None
    if category == 'men_newarrival':
        product_model = MenNewArrival
    elif category == 'women_newarrival':
        product_model = WomenNewArrival
    elif category == 'kids_newarrival':
        product_model = KidsNewArrival
    # ... (repeat for all other categories)

    if product_model:
        specific_product = get_object_or_404(product_model, pk=pk)
        
        product, created = Product.objects.get_or_create(
            title=specific_product.title,
            description=specific_product.description,
            price=specific_product.price,
            category=category,
            image=specific_product.image
        )
        
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

@login_required
def order_success(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        card_number = request.POST.get('card_number')
        expiry_date = request.POST.get('expiry_date')
        cvv = request.POST.get('cvv')
        selected_items = request.POST.getlist('selected_items')
        cart_items = CartItem.objects.filter(id__in=selected_items, user=request.user)
        total_price = sum(item.product.price * item.quantity for item in cart_items)

        # Validate billing information
        if not full_name or not card_number or not expiry_date or not cvv:
            return redirect('transaction_failed')

        if len(card_number) != 16 or not card_number.isdigit() or len(cvv) != 3 or not cvv.isdigit():
            return redirect('transaction_failed')

        # Save billing information
        billing_info = BillingInfo.objects.create(
            user=request.user,
            full_name=full_name,
            card_number=card_number,
            expiry_date=expiry_date,
            cvv=cvv
        )

        # Create order
        order = Order.objects.create(user=request.user, total_price=total_price)
        order.items.set(cart_items)
        order.save()

        # Update product quantities
        for item in cart_items:
            product = item.product
            product.quantity -= item.quantity
            product.save()

        # Clear cart
        cart_items.delete()

        return redirect('payment_success')  # Redirect to the new payment success page

    return render(request, 'order_success.html')

def transaction_success(request):
    return render(request, 'payment_success.html')  # Render the new payment success template

def transaction_failed(request):
    return render(request, 'transaction_failed.html')
