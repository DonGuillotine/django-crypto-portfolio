from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages, auth
from django.contrib.auth.forms import UserCreationForm
from authentication.forms import RegisterForm
from referrals.models import Referral

# Function to handle Login
def login(request):
    if request.method == "POST":
        #  If the request method is post get user details
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print("success")
            messages.success(request, "You have been successfully logged in.")
            return redirect('holdings')
        else:
            messages.error(request, "There was an error loggin in. Please try again.")
            return redirect('login')

    else:
        return render(request, 'authentication/login.html', {})


#  Function to Log User Out
@login_required(login_url='login')
def logout_user(request):
    auth.logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect('home')


#  Function to register a User
def register(request):
    referral_code = request.GET.get('ref')
    if referral_code:
        try:
            referral = Referral.objects.get(referral_code=referral_code, used_by=None)
            referral.used_by = request.user
            referral.save()
            messages.add_message(request, messages.SUCCESS, 'Yay! You received $50 from the referral link.')
        except Referral.DoesNotExist:
            pass
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            auth.login(request, user)
            messages.success(request, ("Registration successful!"))
            return redirect("holdings")
    else:
        form = RegisterForm()

    return render(request, 'authentication/register.html', {
        'form':form
    })