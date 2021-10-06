from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.urls import reverse


# Class to use the forms module
"""forms.Form indicates that the form inherits a class called Form that
is included in the forms module.
Django provides simple server-side validation, on validation tha occurs
once form data has reached the server."""


class NewTaskForm(forms.Form):
    # task and priority fields will collect the information of the user
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=5)


# Create your views here.
def index(request):

    # Check if there already exists a "tasks" key in our session
    if "tasks" not in request.session:

        # if not, create a new list
        request.session["tasks"] = [[]]

    return render(request, "formValidationSession/index.html", {
        "tasks": request.session["tasks"]
    })


def add(request):

    # If method is post
    if request.method == "POST":

        # Take in the data the user submitted and save it as a form
        form = NewTaskForm(request.POST)

        # Check if form data is valid (server-side)
        if form.is_valid():

            # Isolate the task and priority from the 'cleaned' version of form
            # data
            task = form.cleaned_data["task"]
            priority = form.cleaned_data["priority"]

            # Add the new task to our list of tasks using request.session
            request.session["tasks"] += [[task, priority]]

            # Redirect user to list of tasks
            return HttpResponseRedirect(reverse("formValidationSession:index"))

        else:

            # If the form is invalid, re-render the page with the existing
            # information

            return render(request, "formValidationSession/add.html", {
                # Includes NewTaskForm  in the context while rendering the add
                # page
                "form": form
            })

    return render(request, "formValidationSession/add.html", {
        "form": NewTaskForm()
    })
