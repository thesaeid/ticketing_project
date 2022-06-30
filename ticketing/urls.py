from django.urls import path
from .views import index, submit_ticket, user_tickets, admin_view_ticket,admin_view_all_tickets

urlpatterns = [
    path("", index),
    path("submit_ticket/", submit_ticket),
    path("user_tickets/", user_tickets),
    path("admin_view_ticket/", admin_view_ticket),
    path("admin_view_all_tickets/<int:pk>", admin_view_all_tickets),
]
