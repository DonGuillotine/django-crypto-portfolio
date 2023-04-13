from django.shortcuts import render, redirect
from .models import Holding
from .positions import *
from .helper_functions import get_price, get_fg, txtToArray, cum_up_or_down
from .forms import HoldingForm
from datetime import date
import os



