from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("men/", views.men, name="men"),
    path("contact-us/", views.contact, name="contact"),
    path("newarrival/", views.new_arrivals, name="newarrival"),
    path("newarrival/<int:pk>/", views.product_detail, name="product_detail"),
    path("add_to_cart/<int:pk>/", views.add_to_cart, name="add_to_cart"),
    path("add_to_wishlist/<int:pk>/", views.add_to_wishlist, name="add_to_wishlist"),
    path("cart/", views.cart_view, name="cart"),
    path("wishlist/", views.wishlist_view, name="wishlist"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),
    
]