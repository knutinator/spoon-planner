from django import forms
from .models import DailyEnergy


class DailyEnergyForm(forms.ModelForm):
    class Meta:
        model = DailyEnergy
        fields = ['user_energy']
