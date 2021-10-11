from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewFlight, NewBooking
from .models import Flights, Booking
from django.contrib import messages


# Create your views here.


def logbookMain(request):
    flights = Flights.objects.all()
    current_user = request.user
    bookings = Booking.objects.all().order_by('date')
    context = {
        'flights': flights,
        'current_user': current_user,
        'bookings': bookings,
    }
    return render(request, "logbook/index.html", context)


def addFlight(request):
    if request.method == 'POST':
        form = NewFlight(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your flight has been added successfully. Thank you.')
            return redirect('home')
    form = NewFlight()
    context = {
        'form': form
    }
    return render(request, "logbook/form.html", context)


def editFlight(request, flight_id):
    flight = get_object_or_404(Flights, id=flight_id)
    if request.method == 'POST':
        form = NewFlight(request.POST, instance=flight)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = NewFlight(instance=flight)
    context = {
        'form': form,
        'flight': flight,
    }
    return render(request, "logbook/edit.html", context)


def deleteFlight(request, flight_id):
    flight = get_object_or_404(Flights, id=flight_id)
    flight.delete()
    messages.add_message(request, messages.SUCCESS, 'Your flight has been deleted successfully. Thank you.')
    return redirect('home')


def bookFlight(request):
    if request.method == 'POST':
        form = NewBooking(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your booking has been added successfully. Thank you.')
            return redirect('home')
    form = NewBooking()
    context = {
        'bookingForm': form
    }
    return render(request, "logbook/book.html", context)


def editBooking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        form = NewBooking(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = NewBooking(instance=booking)
    context = {
        'bookingForm': form,
        'booking': booking,
    }
    return render(request, "logbook/edit-booking.html", context)


def deleteBooking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    messages.add_message(request, messages.SUCCESS, 'Your booking has been deleted successfully. Thank you.')
    return redirect('home')


def calender(request):
    bookings = Booking.objects.all()
    context = {
        'bookings': bookings
    }
    return render(request, "logbook/calender.html", context)