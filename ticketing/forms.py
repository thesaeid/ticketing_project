from django import forms
from .models import Ticketing, ResponseTicket


class UserSubmitTicketForm(forms.ModelForm):
    class Meta:
        model = Ticketing
        fields = ("title", "phone_number", "description", "user")


class AdminViewTicketForm(forms.Form):
    message = forms.CharField(max_length=32, required=True)
