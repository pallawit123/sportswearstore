from django.contrib import admin
from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [
    path("", views.index, name="myapp"),  # Home page
     path("New Arrivals", views.newarrival, name="New Arrivals"),    # New Arrival page
     path("men/", views.men, name="men"),  # Men category (if needed)
     path("women/", views.women, name="women"),  # Women category (if needed)
    path("contact-us/", views.contact, name="contact"),
    # path('detail/<int:image_id>/', views.detail, name='detail'),
    # path("/contact-us/", views.contact, name="contact")
    # Contact page (if needed)
    # search ko laagi
    #  path('search/', views.search_results, name='search_results'),
]

