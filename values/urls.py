from django.urls import path, include
from . import views


urlpatterns = [
    path("values/", views.values, name="values")
]
