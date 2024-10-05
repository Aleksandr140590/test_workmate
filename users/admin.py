from django.contrib import admin

from users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    """Админка для модели пользователя"""

    list_display = ("username", "email", "first_name", "last_name")
