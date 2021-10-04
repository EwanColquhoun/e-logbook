from django.shortcuts import render

# Create your views here.


def logbookMain(request):
    return render(request, "logbook/index.html")