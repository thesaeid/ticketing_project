from django import forms
from .models import Ticketing,ResponseTicket


class UserSubmitTicketForm(forms.ModelForm):
    class Meta:
        model = Ticketing
        fields = ("title", "phonnum", "description")



class AdminViewTicketForm(forms.ModelForm):
    class Meta:
        model = ResponseTicket
        fields = ("message",)