from django.db import models

# Create your models here.


class Flights(models.Model):
    B744 = 'B744'
    E190 = 'E190'
    E170 = 'E170'
    S2000 = 'S2000'
    J41 = 'J41'
    AIRCRAFT = [
        (B744, 'Boeing 747'),
        (E190, 'Embraer 190'),
        (E170, 'Embraer 170'),
        (S2000, 'Saab 2000'),
        (J41, 'BAE Jetstream 41'),
    ]
    date = models.DateField(null=True)
    captain = models.CharField(max_length=25, default='', blank=False)
    aircraft = models.CharField(max_length=5, choices=AIRCRAFT, default=B744)
    departure = models.CharField(max_length=5, default='', null=False, blank=False)
    destination = models.CharField(max_length=5, null=False, default='', blank=False)
    notes = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.date
