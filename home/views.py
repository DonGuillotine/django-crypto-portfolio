from django.shortcuts import render

# Render home page
def index(request):
    return render(request, 'home.html')