from django.urls import path
from . import views

# To avoid namespace coallition definition
app_name = "formValidationSession"

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add"),
]
