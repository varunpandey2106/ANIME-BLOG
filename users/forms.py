from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import  User
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email= forms.EmailField()

    class Meta: #keeps configurations in one place
        model= User #whenever form validates it creates a new user
        fields= [ 'username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
        email= forms.EmailField()

        class Meta: 
            model= User 
            fields= [ 'username', 'email'] #only update username and email

class ProfileUpdateForm(forms.ModelForm):
      
      class Meta:
           model=Profile
           fields=['image']

    



    

