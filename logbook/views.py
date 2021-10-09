from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewFlight
from .models import Flights
from django.contrib import messages


# Create your views here.


def logbookMain(request):
    flights = Flights.objects.all()
    current_user = request.user
    context = {
        'flights': flights,
        'current_user': current_user,
    }
    return render(request, "logbook/index.html", context)


def addFlight(request):
    if request.method == 'POST':
        form = NewFlight(request.POST)
        if form.is_valid():
            form.save()
            # messages.info(request, 'New flight saved successfully!')
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
    return redirect('home')
