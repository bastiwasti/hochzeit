from django import forms
from .models import Eintrag

class NameForm(forms.ModelForm):

    class Meta:
            model = Eintrag
            fields = ['Name','Anmeldung','Email']