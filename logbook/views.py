from django.shortcuts import render, redirect
from .forms import NewFlight
from .models import Flights

# Create your views here.


def logbookMain(request):
    flights = Flights.objects.all()
    context = {
        'flights': flights
    }
    return render(request, "logbook/index.html", context)


def addFlight(request):
    if request.method == 'POST':
        form = NewFlight(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = NewFlight()
    context = {
        'form': form
    }
    return render(request, "logbook/form.html", context)