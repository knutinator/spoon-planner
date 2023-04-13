from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import DailyEnergy


class DailyEnergyForm(forms.ModelForm):
    user_energy = forms.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)]
    )

    class Meta:
        model = DailyEnergy
        fields = ['user_energy']
