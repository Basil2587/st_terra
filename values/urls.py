from django.urls import path, include

from results.views import index
from values.views import values

urlpatterns = [
    path("", index, name="index"),
    path("values/", values, name="values")
]
