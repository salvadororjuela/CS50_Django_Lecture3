from django.shortcuts import render
import datetime


# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, "newyearStyle/index.html", {
        "newyear": now.month and now.day == 1
    })
