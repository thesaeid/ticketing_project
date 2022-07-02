from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
from .forms import AdminViewTicketForm, UserSubmitTicketForm
from .models import Ticketing, ResponseTicket
from django.core.mail import send_mail
from django.contrib import messages


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        queryset = Ticketing.objects.all()
        checked_tickets_count = queryset.filter(status="بررسی شده").count()
        inprogress_tickets_count = queryset.filter(status="درحال بررسی").count()
        not_checked_tickets_count = queryset.filter(status="بررسی نشده").count()
        return render(
            request,
            "ticketing/index/index.html",
            {
                "tickets": queryset,
                "checked_tickets_count": checked_tickets_count,
                "inprogress_tickets_count": inprogress_tickets_count,
                "not_checked_tickets_count": not_checked_tickets_count,
            },
        )
    else:
        return redirect("/login")


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


@login_required
def user_tickets(request, pk):
    tickets = Ticketing.objects.filter(user_id=pk)
    user = Ticketing.objects.select_related("user").filter(user__id=pk)
    return render(
        request,
        "ticketing/user_tickets/user_tickets.html",
        {tickets: "tickets", user: "user"},
    )


@login_required
def admin_view_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticketing, id=ticket_id)
    if request.method == "POST":
        form = AdminViewTicketForm(request.POST)
        if form.is_valid():
            message = form.data.get("message")
            if form.data.get("status_check"):
                ticket.status = "بررسی شده"
                ticket.save()
            elif form.data.get("status_inp"):
                ticket.status = "درحال بررسی"
                ticket.save()
            elif form.data.get("status_not_checked"):
                ticket.status = "بررسی نشده"
                ticket.save()

            if ResponseTicket.objects.filter(ticket__id=ticket_id).exists():
                response = ResponseTicket.objects.filter(ticket__id=ticket_id).first()
                response.message = message
                response.ticket = ticket
                response.save()
            else:
                ResponseTicket.objects.create(ticket=ticket, message=message)

            return redirect("/")
    else:
        form = AdminViewTicketForm()
    return render(
        request,
        "ticketing/admin_view_ticket/admin_view_ticket.html",
        {"form": form, "ticket": ticket},
    )


@login_required
def admin_view_all_tickets(request):
    tickets = Ticketing.objects.all()
    return render(
        request,
        "ticketing/admin_view_all_tickets/admin_view_all_tickets.html",
        {"tickets": tickets},
    )


@login_required
def logout(request):
    django_logout(request)
    return redirect("login")
