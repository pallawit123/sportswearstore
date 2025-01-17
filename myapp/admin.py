from django.contrib import admin
from .models import Contact, NewArrival

admin.site.register(Contact)

@admin.register(NewArrival)
class NewArrivalAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'created_at']
    search_fields = ['title', 'description']