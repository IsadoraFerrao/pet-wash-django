from django import forms
from booking.models import Booking
from datetime import date

class BookingForm(forms.ModelForm):
    def clean_data(self):
        Date = self.cleaned_data['date']
        today = date.today()
        if Date < today:
            raise forms.ValidationError('You cannot book a bath on a day from the past.')
        return Date

    class Meta:
        model = Booking
        fields = [
            'name', 'email', 'pet_name', 'date', 'shift', 'branch', 'size', 'notes'
        ]