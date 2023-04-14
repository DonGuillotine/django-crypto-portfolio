from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Referral
from django.urls import reverse

@login_required
def referral_link(request):

    #   Generates a unique referral link for the currently logged-in user and displays it on the screen.
    referral, created = Referral.objects.get_or_create(referrer=request.user)
    referral_link = request.build_absolute_uri(reverse('register') + '?ref=' + referral.referral_code)
    return render(request, 'referral/link.html', {'referral_link': referral_link})