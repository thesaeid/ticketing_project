from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator


class Category(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return str(self.name)


class Ticketing(models.Model):
    baresi = 1
    darhal_baresi = 2
    baresi_nashode = 3

    STATUS_CHOICES = (
        (baresi, "بررسی شده"),
        (darhal_baresi, "درحال بررسی"),
        (baresi_nashode, "بررسی نشده"),
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="users"
    )
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=32)
    status = models.CharField(
        max_length=32, default="بررسی نشده", choices=STATUS_CHOICES
    )
    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
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
    ticket = models.OneToOneField(
        Ticketing, on_delete=models.CASCADE, related_name="ticket"
    )
    message = models.CharField(max_length=32, default="", null=True, blank=True)
