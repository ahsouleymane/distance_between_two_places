from django import forms
from .models import *

class coordonneesForm(forms.ModelForm):
    class Meta:
        model = Coordonnees
        fields = ['emplacement', 'latitude', 'longitude']
        labels = {
            'emplacement': 'Nom Emplacement',
            'latitude': 'Latitude',
            'longitude': 'Longitude',
        }
