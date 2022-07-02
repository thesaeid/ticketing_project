from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import CustomUser
from .forms import Login

# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "GET":
        form = Login()
        return render(request, "authenticating/form/login.html", {"form": form})

    elif request.method == "POST":
        form = Login(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = get_object_or_404(CustomUser, email=email, password=password)
            if user is not None:
                login(request, user)
                if (
                    user.email == "admin@ticket.com"
                    and user.password == form.cleaned_data["password"]
                ):
                    return redirect("/")

                elif (
                    user.email == "user@ticket.com"
                    and user.password == form.cleaned_data["password"]
                ):
                    return redirect("submit_ticket")

                else:
                    form = Login()
                    messages.add_message(
                        request, messages.ERROR, "Invalid email or password"
                    )

                    return render(
                        request,
                        "authenticating/form/login.html",
                        {"form": form},
                    )
