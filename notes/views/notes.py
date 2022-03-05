from django.shortcuts import render, redirect
from django.contrib import messages


from notes.models import Notes


def dashboard(request):
    notes = Notes.objects.filter(user=request.user)
    print(notes)
    return render(request, "dashboard.html",{"notes":notes})

def add_notes(request):
    if request.method=="POST":
        title=request.POST.get('title')
        notes=request.POST.get('description')
        note = Notes(title=title, notes=notes, user=request.user)
        note.save()                             
        messages.add_message(request, messages.SUCCESS, 'Registered successfully')
        return redirect(dashboard)

    else:
        return render(request, "add_notes.html")

def update_notes(request, id):
    if request.method=="POST":
        title=request.POST.get('title')
        notes=request.POST.get('description')

        note = Notes()
        note.title=title
        note.notes=notes
        note.user=request.user
        note.save()                             
        messages.add_message(request, messages.SUCCESS, 'Registered successfully')
        return redirect(dashboard)

    else:

        return render(request, "update_notes.html")