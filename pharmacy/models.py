from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.urls import reverse


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    class Meta:
        ordering = ["country"]

    def __str__(self):
        return f"Name: {self.name} | Country: {self.country}"


class Department(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)
    phone = models.IntegerField(unique=True, null=True)
    address = models.CharField(max_length=255, unique=True)
    name_pharmacy = models.CharField(max_length=255)
    time_work = models.CharField(max_length=255)

    class Meta:
        verbose_name = "department"
        verbose_name_plural = "departments"

    def __str__(self):
        return (
            f"{self.username} ({self.first_name}"
            f" {self.last_name}, licence number: {self.license_number}"
        )

    def get_absolute_url(self):
        return reverse("pharmacy:department-detail", kwargs={"pk": self.pk})


class Medicine(models.Model):
    name = models.CharField(max_length=255, blank=True)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, related_name="medicines"
    )
    departments = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="medicines"
    )
    price = models.DecimalField(max_digits=6, decimal_places=2)
    amount_medicine = models.IntegerField()

    class Meta:
        ordering = ["-amount_medicine"]

    def __str__(self):
        return f"Model: {self.name}; Manufacturer: {self.manufacturer.name}"
