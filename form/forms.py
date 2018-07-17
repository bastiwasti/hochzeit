from django import forms
from .models import Eintrag

class NameForm(forms.ModelForm):

    class Meta:
            model = Eintrag
            fields = ['Anmeldung', 'Essen','Email']