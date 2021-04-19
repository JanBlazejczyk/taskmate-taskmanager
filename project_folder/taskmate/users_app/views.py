from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def register(request):
    # our form which is the instance of custom form class
    register_form = UserCreationForm()
    context = {
        'register_form': register_form
    }
    return render(request, "register.html", context)
