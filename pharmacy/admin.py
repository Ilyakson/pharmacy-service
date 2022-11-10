from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from pharmacy.models import Manufacturer, Account, Medicine


admin.site.register(Manufacturer)


@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ["model", "manufacturer"]
    list_filter = ["manufacturer"]
    search_fields = ["model"]


@admin.register(Account)
class AccountAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("license_number",)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Additional info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "license_number",
                )
            },
        ),
    )