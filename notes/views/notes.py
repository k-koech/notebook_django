from django.shortcuts import render


def dashboard(request):
    return render(request, "dashboard.html")

def add_notes(request):
    return render(request, "add_notes.html")