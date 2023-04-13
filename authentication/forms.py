from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


#  Created User Registration Class
class RegisterForm(UserCreationForm):
    class Meta:
        model = User

        fields = ("username", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["class"] = "form-control"