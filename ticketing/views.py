from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import UserSubmitTicketForm
from .models import Ticketing

# Create your views here.
def index(request):
    return render(request, "ticketing/index/index.html")


@login_required
def submit_ticket(request):
    if request.user.is_authenticated:
        email = request.user.email
        print(email)
        user = Ticketing.objects.select_related("user").filter(user__email=email)
        if request.method == "POST":
            form = UserSubmitTicketForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("/ticketing/user_tickets/")
            else:
                print(form.data)
                return HttpResponse("not ok")
        else:
            form = UserSubmitTicketForm()

    return render(
        request,
        "ticketing/user_tickets/user_tickets.html",
        {"form": form, "email": "user.email"},
    )


def user_tickets(request):
    return render(request, "ticketing/user_tickets/user_tickets.html")


def admin_view_ticket(request):
    return render(request, "ticketing/admin_view_ticket/admin_view_ticket.html")

def admin_view_all_tickets(request):
    return render(request, "ticketing/admin_view_all_tickets/admin_view_all_tickets.html")
