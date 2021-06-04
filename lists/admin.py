from django.contrib import admin

from .models import ListType, MyList


class ListTypeAdmin(admin.ModelAdmin):
    list_display = ("pk", "title")
    empty_value_display = "-пусто-"


class MyListAdmin(admin.ModelAdmin):
    list_display = ("pk", "author", "title", "type", "done", "favorite")
    empty_value_display = "-пусто-"


admin.site.register(ListType, ListTypeAdmin)
admin.site.register(MyList, MyListAdmin)
