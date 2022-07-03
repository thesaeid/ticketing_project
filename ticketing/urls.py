from django.urls import path
from .views import (
    index,
    submit_ticket,
    user_tickets,
    admin_view_ticket,
    admin_view_all_tickets,
    logout,
    view_ticket,
    home,
)

urlpatterns = [
    path("index/", index, name="index"),
    path("", home, name="home"),
    path("view_ticket/<int:ticket_id>", view_ticket, name="view_ticket"),
    path("submit_ticket/", submit_ticket, name="submit_ticket"),
    path("user_tickets/", user_tickets, name="user_tickets"),
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
