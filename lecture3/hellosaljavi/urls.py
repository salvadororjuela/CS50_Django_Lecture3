from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("salvador", views.salvador, name="salvador"),
    path("javier", views.javier, name="javier")
]
