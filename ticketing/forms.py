from django import forms
from .models import Ticketing, ResponseTicket


class UserSubmitTicketForm(forms.Form):
    title = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=17)
    description = forms.CharField(widget=forms.Textarea)


class AdminViewTicketForm(forms.Form):
    message = forms.CharField(max_length=32, required=True)
