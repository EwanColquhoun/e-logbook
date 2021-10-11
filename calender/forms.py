from django import forms
from .models import Events


class DateInput(forms.DateInput):
    input_type = 'date'


class NewEvent(forms.ModelForm):
    class Meta:
        model = Events
        fields = ['name', 'start', 'end']
        widgets = {
            'date': DateInput(),
        }
