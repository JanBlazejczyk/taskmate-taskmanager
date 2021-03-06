from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        register_form = CustomUserCreationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(
                request, "New User Account Created, Log In to Get Started")
            return redirect('register')
    else:
        # our form which is the instance of custom form class
        register_form = CustomUserCreationForm()

    return render(request, "register.html", {'register_form': register_form})
