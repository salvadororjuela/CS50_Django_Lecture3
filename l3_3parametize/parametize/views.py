from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, "hola/index.html")


def greet(request, name):
    return render(request, "hola/greet.html", {
        "name": name.upper()
    })
