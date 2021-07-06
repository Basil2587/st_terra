from django.contrib import admin

from .models import MyGoals


class MyGoalsAdmin(admin.ModelAdmin):
    list_display = ("pk", "author", "text", "sphere", "date", "image")
    empty_value_display = "-пусто-"


admin.site.register(MyGoals, MyGoalsAdmin)
