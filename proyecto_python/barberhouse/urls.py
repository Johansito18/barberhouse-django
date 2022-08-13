from unicodedata import name
from django.urls import path

from . import views

app_name = "barberhouse"

urlpatterns = [
    path('', views.inicio, name="inicio"),
]
