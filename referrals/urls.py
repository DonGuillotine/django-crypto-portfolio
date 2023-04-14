from django.urls import path

from . import views

urlpatterns = [
    path('referral', views.referral_link, name='referral'),
]