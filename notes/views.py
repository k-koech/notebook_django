from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "index.html")

def signup(request):
    return render(request, "signup.html")

def signin(request):
    return render(request, "signin.html")

def dashboard(request):
    return render(request, "dashboard.html")