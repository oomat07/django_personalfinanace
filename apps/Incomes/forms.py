from django import forms
from .models import Income

class IncomeForm(forms.Modelform):
    class Meya:
        model = Income
        fields = ['source', 'amount', 'date', 'description']