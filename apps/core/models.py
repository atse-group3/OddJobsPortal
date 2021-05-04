from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

def sendEmail(request):
    password = request.POST.get('password')
    username = request.POST.get('username')
    email = request.POST.get('email')
    user = get_user_model().objects.create(username = username, password = password, email = email)
    sendConfirm(user)
    return render (request, 'confirm_template.html')
    

