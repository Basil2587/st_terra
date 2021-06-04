from django.contrib import admin

from .models import Target, Plan, Diary


class PlanAdmin(admin.ModelAdmin):
    list_display = ("pk", "author", "title", "done", "date")
    empty_value_display = "-пусто-"


class TargetAdmin(admin.ModelAdmin):
    list_display = ("pk", "author", "title", "done", "date")
    empty_value_display = "-пусто-"


class DiaryAdmin(admin.ModelAdmin):
    list_display = ("pk", "conclusion", "achievements", "good_things", "date")
    empty_value_display = "-пусто-"


admin.site.register(Plan, PlanAdmin)
admin.site.register(Target, TargetAdmin)
admin.site.register(Diary, DiaryAdmin)
