from django import forms
from .models import Ticketing


class UserSubmitTicketForm(forms.ModelForm):
    class Meta:
        model = Ticketing
        fields = ("title", "phonnum", "description")