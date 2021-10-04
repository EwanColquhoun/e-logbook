from django import forms
from .models import Flights


class DateInput(forms.DateInput):
    input_type = 'date'


class NewFlight(forms.ModelForm):
    class Meta:
        model = Flights
        fields = fields = '__all__'
        widgets = {
            'date': DateInput(),
        }
