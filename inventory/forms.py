from django import forms
from .models import Chicken, Egg

class ChickenForm(forms.ModelForm):
    class Meta:
        model = Chicken
        fields = ['name', 'age', 'breed', 'health_status']

class EggForm(forms.ModelForm):
    class Meta:
        model = Egg
        fields = ['quantity', 'date_collected']
