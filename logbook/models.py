from django.db import models
from django.conf import settings
from django.contrib.auth.models import User  # Used to get the default users model from django

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
    captain = models.CharField(max_length=25, default='', null=False, blank=False)
    aircraft = models.CharField(max_length=5, choices=AIRCRAFT, default=B744)
    departure = models.CharField(max_length=5, default='', null=False, blank=False)
    destination = models.CharField(max_length=5, null=False, default='', blank=False)
    duration = models.TimeField(default='01:00')
    notes = models.CharField(max_length=50, default='', blank=True)

    def __str__(self):
        return self.captain


class Slots(models.Model):
    SLOTS = [
        ('7-8', '0700-0800'),
        ('9-10', '0900-1000'),
        ('11-12', '1100-1200'),
        ('12-14', '1300-1400'),
        ('14-16', '1500-1600'),
    ]
    slot = models.CharField(max_length=15, choices=SLOTS, default=False)

    def __str__(self):
        return self.slot


class Booking(models.Model):
    TRAINERS = [
        ('PA-28', 'Piper Warrier'),
        ('C150', 'Cessna 150'),
        ('Cub', 'Piper Cub'), 
    ]

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, default='')
    aircraft = models.CharField(max_length=5, choices=TRAINERS, default='PA-28')
    date = models.DateField(null=True)
    slot = models.ForeignKey(Slots, on_delete=models.CASCADE, default=False, related_name='slot_booking')
    notes = models.TextField(default='')


    def __str__(self):
        return self.name
