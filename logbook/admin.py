from django.contrib import admin
from .models import Flights, Booking
# Register your models here.


@admin.register(Flights)
class FlightsAdmin(admin.ModelAdmin):

    list_display = ('date', 'captain', 'aircraft', 'departure', 'destination', 'duration')
    list_filter = ('captain', 'date', 'destination', 'departure', 'aircraft')
    search_fields = ['captain', 'date', 'destination', 'departure', 'aircraft']



@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = ('date', 'name', 'aircraft', 'email')
    list_filter = ('date', 'name', 'aircraft', 'email')
