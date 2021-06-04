from django.contrib import admin

from .models import GoalType, MyGoals


class GoalTypeAdmin(admin.ModelAdmin):
    list_display = ("pk", "title")
    empty_value_display = "-пусто-"


class MyGoalsAdmin(admin.ModelAdmin):
    list_display = ("pk", "author", "text", "type", "image")
    empty_value_display = "-пусто-"


admin.site.register(GoalType, GoalTypeAdmin)
admin.site.register(MyGoals, MyGoalsAdmin)
