from django.contrib import admin
from django.contrib.auth import get_user_model
from users.models import User
#User = get_user_model


class UserAdmin(admin.ModelAdmin):
    list_display = ("pk", "username")
    empty_value_display = "-пусто-"


admin.site.register(User, UserAdmin)
