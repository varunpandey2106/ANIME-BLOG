from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required #provided by django
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm 
from django.core.mail import send_mail
from django.conf import settings
from django.conf import settings

# Create your views here.

def register(request):
    if request.method == 'POST':
        form= UserRegisterForm(request.POST)  #instantiate user creation form with POST data
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get("username") #validated form data is in form.cleaned_data dictionary
            messages.success(request, f'Your account is now created and you can login!') #flash message
            return redirect('login')
    else:
        form= UserRegisterForm()
    
    form= UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form= UserUpdateForm(request.POST,instance=request.user)
        p_form= ProfileUpdateForm( request.POST,request.FILES,instance=request.user.profile)
        #to access these within the template we make a context dictionary, keys are variables that we will access with the template

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your profile information was successfuly updated!') #flash message
            return redirect('profile') #redirect because of POST GET redirect pattern
            #redirect causes a GET request and prevents the usual POST request( if you refresh data about be resubmitted)
    else:
        u_form= UserUpdateForm(instance=request.user)
        p_form= ProfileUpdateForm( instance=request.user.profile)

    context={
        'u_form': u_form,
        'p_form': p_form, 
    }
    return render(request, 'users/profile.html', context)


def send_email_to_client():
    subject="password reset email"
    message="you can reset your password now!"
    from_email= settings.EMAIL_HOST_USER
    recipient_list=["varun.pandey2106@gmail.com"]

    send_mail(subject,message,from_email,recipient_list)