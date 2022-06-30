from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "ticketing/index/index.html")


def submit_ticket(request):
    return render(request, "ticketing/submitticket/submitticket.html")


def user_tickets(request):
    return render(request, "ticketing/user_tickets/user_tickets.html")


def admin_view_ticket(request):
    return render(request, "ticketing/admin_view_ticket/admin_view_ticket.html")
