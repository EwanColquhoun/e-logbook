from django import forms
from .models import Flights, Booking


class DateInput(forms.DateInput):
    input_type = 'date'


# class TimeField(forms.TimeField):
#     input_type = 'duration'


class NewFlight(forms.ModelForm):
    class Meta:
        model = Flights
        fields = fields = '__all__'
        widgets = {
            'date': DateInput(),
            
        }


class NewBooking(forms.ModelForm):
    class Meta:
        model: Booking
        fields = ('date', 'aircraft', 'name', 'email')
