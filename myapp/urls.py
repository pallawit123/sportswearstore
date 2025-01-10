from django.contrib import admin
from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [
    path("", views.index, name="myapp"),  # Home page
    path("newarrival/", views.newarrival, name="newarrival"),    # New Arrival page
    path("men/", views.men, name="men"),  # Men category (if needed)
    path("women/", views.women, name="women"),  # Women category (if needed)
    path("contact-us/", views.contact, name="contact"),
]
