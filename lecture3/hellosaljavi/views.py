from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello!!!!!!")


def salvador(request):
    return HttpResponse("Hola, Salvadorrrrrrr!!!!!!")


def javier(request):
    return HttpResponse("HOLA, JAVIIIIII!!!!!!!!!!!!1")
