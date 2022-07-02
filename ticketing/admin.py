from django.contrib import admin
from ticketing.models import Ticketing, Category


class TicketingAdmin(admin.ModelAdmin):
    list_display = ["user", "title", "status", "description"]


admin.site.register(Ticketing, TicketingAdmin)
