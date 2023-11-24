from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.contrib import messages

from .models import UserProfile

from .forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm

from django.conf import settings
from seeds import generate_stock_data

DEFAULT_PROFILE_DIR = "images/profiles/default_profile.png"

# Create your views here.

def signup_view(response):
    if response.user.is_authenticated: # Already logged in
        return redirect("home")

    if response.method == "POST":
        user_form = SignupForm(response.POST)

        if user_form.is_valid():
            user_form.save()

            new_user = authenticate(username=user_form.cleaned_data['username'],
                                    password=user_form.cleaned_data['password1'],
                                    )

            # Create an empty UserProfile associated with the User
            user_profile = UserProfile(user=new_user)
            user_profile.save()

            if settings.DEBUG == True:
                generate_stock_data(new_user, 15)

            login(response, new_user)

            messages.info(response, "Thanks for signing up! You are now logged in.")

            return redirect("home")
    else:
        user_form = SignupForm()
    
    return render(response, "signup.html", {'user_form': user_form})

def login_view(response):
    if response.method == 'POST':
        form = AuthenticationForm(response, data=response.POST)
        
        if form.is_valid():

            login(response, form.get_user())

            messages.success(response, "Successfully logged in!")

            return redirect("home")
        else:
            messages.error(response, 'Incorrect username/password.')
    else:
        form = AuthenticationForm()

    return render(response, 'login.html', {'form': form})

@login_required
def profile_view(response):
    profile_picture = ""
    if response.user.userprofile.profile_picture == "":
        profile_picture = DEFAULT_PROFILE_DIR
    else:
        profile_picture = response.user.userprofile.profile_picture

    return render(response, "profile.html", {'user': response.user, 'profile_picture': profile_picture})

def logout_view(response):
    logout(response)

    return render(response, "logout.html", {'user': response.user})