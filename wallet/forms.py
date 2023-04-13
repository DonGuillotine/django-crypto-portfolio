from xml.dom import ValidationErr
from django import forms
from django.forms import ModelForm, ValidationError
from .models import Holding
from .helper_functions import txtToArray
from datetime import date
from django.utils.translation import gettext_lazy as _