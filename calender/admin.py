from django.contrib import admin
from calender.models import Events

# Register your models here.
@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'start', 'end')
    list_filter = ('id', 'name', 'start', 'end')
    search_fields = ('id', 'name', 'start', 'end')
