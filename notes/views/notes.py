from django.shortcuts import render, redirect
from django.contrib import messages


from notes.models import Notes


def dashboard(request):
    notes = Notes.objects.filter(user=request.user)
    past_notes = Notes.objects.order_by('-date')

    print(notes)
    return render(request, "dashboard.html",{"notes":notes, "past_notes":past_notes})

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

def notes(request, id):
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
        notes = Notes.objects.get(user=request.user, id=id)
        return render(request, "notes.html", {"notes":notes})