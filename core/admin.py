from django.contrib import admin
from .models import Pet, Appointment, Doctor

# Register your models here.
@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'owner_name', 'owner_phone')
    search_fields = ('name', 'owner_name')


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('pet','doctor', 'date','status', 'reason')
    list_filter = ('status', 'doctor', 'date',)
    search_fields = ('pet', 'first_name', 'reason')

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'specialization', 'phone')
    search_fields = ('first_name', 'last_name', 'specialization')