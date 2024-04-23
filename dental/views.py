from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'dental/home.html')

def about(request):
    return render(request, 'dental/about.html')

def contact(request):
    return render(request, 'dental/contact.html')

def services(request):
    return render(request, 'dental/services.html')