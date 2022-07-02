from django.urls import path
from .views import (
    index,
    submit_ticket,
    user_tickets,
    admin_view_ticket,
    admin_view_all_tickets,
    logout,
)

urlpatterns = [
    path("", index, name="index"),
    path("submit_ticket/", submit_ticket, name="submit_ticket"),
    path("user_tickets/<int:pk>/", user_tickets, name="user_tickets"),
    path(
        "admin_view_all_tickets/",
        admin_view_all_tickets,
        name="admin_view_all_tickets",
    ),
    path(
        "admin_view_ticket/<int:ticket_id>/",
        admin_view_ticket,
        name="admin_view_ticket",
    ),
    path("logout/", logout, name="logout"),
]
