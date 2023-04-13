from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


# Function to handle Login
def login(request):
    if request.method == "POST":
        #  If the request method is post get user details
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("success")
            return redirect('holdings')
        else:
            print('failed')
            messages.success(request, "There was an error loggin in. Please try again.")
            return redirect('login')

    else:
        return render(request, 'authenticate/login.html', {})