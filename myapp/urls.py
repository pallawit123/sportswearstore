from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("men/", views.men, name="men"),
    path("contact-us/", views.contact, name="contact"),
    path("newarrival/", views.men_new_arrivals, name="newarrival"),
    path("newarrival/<str:category>/<int:pk>/", views.product_detail, name="product_detail"),
    path("add_to_cart/<str:category>/<int:pk>/", views.add_to_cart, name="add_to_cart"),
    path("add_to_wishlist/<str:category>/<int:pk>/", views.add_to_wishlist, name="add_to_wishlist"),
    path("cart/", views.cart_view, name="cart"),
    path("wishlist/", views.wishlist_view, name="wishlist"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),
    path('profile/', views.profile, name='profile'),
    path("men/newarrival/", views.men_new_arrivals, name="men_newarrival"),
    path("men/autumn-winter/", views.men_autumn_winter, name="men_autumn_winter"),
    path("women/newarrival/", views.women_new_arrivals, name="women_newarrival"),
    path("women/autumn-winter/", views.women_autumn_winter, name="women_autumn_winter"),
    path("kids/newarrival/", views.kids_new_arrivals, name="kids_newarrival"),
    path("kids/autumn-winter/", views.kids_autumn_winter, name="kids_autumn_winter"),
]