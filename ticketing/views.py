from django.http import HttpResponse
from django.shortcuts import redirect, render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import Ticketing
from django.core.mail import send_mail
from django.contrib import messages



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


def user_tickets(request,pk):
    tickets = Ticketing.objects.filter(user_id=pk)
    user = Ticketing.objects.select_related("user").filter(user__id=pk)
    return render(request, "ticketing/user_tickets/user_tickets.html",{tickets:'tickets',user:'user'})


def admin_view_ticket(request,ticket_id):
    ticket = get_object_or_404(Ticketing, id=ticket_id)
    if request.method == 'POST':
        form = AdminViewTicketForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            message = cd['message']
            subject = 'your ticket response !'
            messages.add_message(
                request, messages.ERROR, "Email sent correctly"
            )
            send_mail(subject, message, 'erfankiani10@gmail.com', [ticket.user.email], fail_silently=False)
    else:
        form = AdminViewTicketForm()
    return render(request, 'ticketing/admin_view_ticket/admin_view_ticket.html', {'form': form, 'ticket': ticket})




def admin_view_all_tickets(request,pk):
    tickets=Ticketing.objects.all()
    user = Ticketing.objects.select_related("user").filter(user__id=pk)
    return render(request, "ticketing/admin_view_all_tickets/admin_view_all_tickets.html",{tickets:'tickets',user:'user'})
