from django.contrib import admin
from .models import Flights
# Register your models here.


@admin.register(Flights)
class FlightsAdmin(admin.ModelAdmin):

    list_display = ('date', 'captain', 'aircraft', 'departure', 'destination', 'duration')
    list_filter = ('captain', 'date', 'destination', 'departure', 'aircraft')
    search_fields = ['captain', 'date', 'destination', 'departure', 'aircraft']
