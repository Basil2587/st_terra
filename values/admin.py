from django.contrib import admin

from .models import Algorithm, AlgorithmType, Value, ValueType

class ValueTypeAdmin(admin.ModelAdmin):
    list_display = ("pk", "title")
    empty_value_display = "-пусто-"


class ValueAdmin(admin.ModelAdmin):
    list_display = ("pk", "author", "title", "type")
    empty_value_display = "-пусто-"


admin.site.register(Algorithm, ValueAdmin)
admin.site.register(AlgorithmType, ValueTypeAdmin)
admin.site.register(Value, ValueAdmin)
admin.site.register(ValueType, ValueTypeAdmin)
