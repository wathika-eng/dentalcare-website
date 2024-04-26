from django.shortcuts import render

# import requests


# Create your views here.
def home(request):
    if request.method == "POST":
        name = request.POST.get("message-name")
        email = request.POST.get("message-email")
        message = request.POST.get("message")
        return render(request, "dental/home.html", {"name": name})
    else:
        return render(request, "dental/home.html", {})


def about(request):
    return render(request, "dental/about.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get("message-name")
        email = request.POST.get("message-email")
        message = request.POST.get("message")
        return render(request, "dental/contact.html", {"name": name})

    else:
        return render(request, "dental/contact.html", {})


def services(request):
    return render(request, "dental/services.html")
