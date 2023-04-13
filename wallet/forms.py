from xml.dom import ValidationErr
from django import forms
from django.forms import ModelForm, ValidationError
from .models import Holding
from .helper_functions import txtToArray
from datetime import date
from django.utils.translation import gettext_lazy as _


# The forms for the Holding
class HoldingForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'id':'tags', 'placeholder':'Coin', 'data-bs-toggle':"tooltip", 'data-bs-placement':"top", 'title':"Use an auto-suggestion below"}))
    use_mv_entry = forms.BooleanField(widget=forms.CheckboxInput(attrs={'id':'use_mv_entry', 'name':"use_mv_entry"}), label="use market price", label_suffix="", initial=False, required=False)
    class Meta:
        model = Holding
        fields = ('name', 'entry_price', 'entry_amount')


    widgets = {
            'coin_id': forms.TextInput(attrs={'class':'form-control', 'id':'tags', 'placeholder':'Coin (choose from below)'}),
            'entry_price': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Entry Price', 'name':'entry-price', 'id':'entry-price', 'required':False}),
            'entry_amount': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Entry Amount (USD)'}),
        }