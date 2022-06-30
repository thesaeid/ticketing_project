from authenticating.models import CustomUserManager
from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return str(self.name)


class Ticketing(models.Model):
    baresi = 1
    darhal_baresi = 2
    baresi_nashode = 3

    ATTRIBUTE_TYPE_FIELDS = (
        (baresi, "baresi"),
        (darhal_baresi, "darhal_baresi"),
        (baresi_nashode, "baresi_nashode"),
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="users"
    )
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=32)
    type = models.PositiveSmallIntegerField(
        default=baresi_nashode, choices=ATTRIBUTE_TYPE_FIELDS
    )
    phonnum = models.TextField()
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="categories",
        default="",
        null=True,
    )
    description = models.TextField()

    def __str__(self):
        return str(self.title)


class ResponseTicket(models.Model):
    tickets = models.ForeignKey(
        Ticketing, on_delete=models.CASCADE, related_name="ticket"
    )
    message = models.CharField(max_length=32, default="")
