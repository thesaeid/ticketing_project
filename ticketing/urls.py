from django.urls import path
from .views import index, submit_ticket, user_tickets, admin_view_ticket

urlpatterns = [
    path("", index),
    path("submit_ticket/", submit_ticket),
    path("user_tickets/", user_tickets),
    path("admin_view_ticket/", admin_view_ticket),
]
