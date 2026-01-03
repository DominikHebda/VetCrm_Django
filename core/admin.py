from django.contrib import admin
from .models import Pet, Appointment, Doctor

# Register your models here.
@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'owner_name', 'owner_phone')
    search_fields = ('name', 'owner_name')


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('pet', 'date', 'reason')
    list_filter = ('date',)
    search_fields = ('pet', 'reason')

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'specialization', 'phone')
    search_fields = ('first_name', 'last_name', 'specialization')