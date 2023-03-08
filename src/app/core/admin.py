"""
    Django admin customization.
"""
from core import models
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""

    ordering = ["id"]
    list_display = ["email", "name", "is_deleted"]
    fieldsets = (
        (None, {"fields": ("email", "password", "uuid")}),
        (_("Personal Info"), {"fields": ("name",)}),
        (None, {"fields": ("is_deleted",)}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "created_at", "updated_at", "deleted_at")}),
    )
    readonly_fields = ["last_login", "created_at", "updated_at", "deleted_at", "uuid", "is_deleted"]
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "name",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )


admin.site.register(models.User, UserAdmin)
