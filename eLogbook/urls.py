"""eLogbook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from logbook import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.logbookMain, name='home'),
    path('add', views.addFlight, name='addFlight'),
    path('edit/<flight_id>', views.editFlight, name='editFlight'),
    path('edit-booking/<booking_id>', views.editBooking, name='editBooking'),
    path('delete/<flight_id>', views.deleteFlight, name='delete'),
    path('delete-booking/<booking_id>', views.deleteBooking, name='deleteBooking'),
    path('accounts/', include('allauth.urls')),
    path('book', views.bookFlight, name='book'),
]
