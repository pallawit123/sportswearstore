from django.contrib import admin
from .models import *

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'date']
    search_fields = ['name', 'email', 'phone']

# Men's Category
@admin.register(MenNewArrival)
class MenNewArrivalAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'created_at']
    search_fields = ['title', 'description']

@admin.register(MenAutumnWinter)
class MenAutumnWinterAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title', 'description']

@admin.register(MenTShirts)
class MenTShirtsAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title', 'description']

@admin.register(MenPolos)
class MenPolosAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title', 'description']

@admin.register(MenShorts)
class MenShortsAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title', 'description']

@admin.register(MenTrackpantsJoggers)
class MenTrackpantsJoggersAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title', 'description']

@admin.register(MenRunning)
class MenRunningAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title', 'description']

@admin.register(MenYoga)
class MenYogaAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title', 'description']

# Women's Category
@admin.register(WomenNewArrival)
class WomenNewArrivalAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'created_at']
    search_fields = ['title', 'description']

@admin.register(WomenAutumnWinter)
class WomenAutumnWinterAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title', 'description']

@admin.register(WomenTShirts)
class WomenTShirtsAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title', 'description']

@admin.register(WomenPolos)
class WomenPolosAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title', 'description']

@admin.register(WomenShorts)
class WomenShortsAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title', 'description']

@admin.register(WomenTrackpantsJoggers)
class WomenTrackpantsJoggersAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title', 'description']

@admin.register(WomenRunning)
class WomenRunningAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title', 'description']

@admin.register(WomenYoga)
class WomenYogaAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title', 'description']

# Kids' Category
@admin.register(KidsNewArrival)
class KidsNewArrivalAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'created_at']
    search_fields = ['title', 'description']

@admin.register(KidsAutumnWinter)
class KidsAutumnWinterAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title', 'description']

@admin.register(KidsTShirts)
class KidsTShirtsAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title', 'description']

@admin.register(KidsPolos)
class KidsPolosAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title', 'description']

@admin.register(KidsShorts)
class KidsShortsAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title', 'description']

@admin.register(KidsTrackpantsJoggers)
class KidsTrackpantsJoggersAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title', 'description']

@admin.register(KidsRunning)
class KidsRunningAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title', 'description']

@admin.register(KidsYoga)
class KidsYogaAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title', 'description']

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'quantity']
    search_fields = ['user__username', 'product__title']

@admin.register(WishlistItem)
class WishlistItemAdmin(admin.ModelAdmin):
    list_display = ['user', 'product']
    search_fields = ['user__username', 'product__title']