from django.contrib import admin
from .models import Pet

# Register your models here.
@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'owner_name', 'owner_phone')
    search_fields = ('name', 'owner_name')