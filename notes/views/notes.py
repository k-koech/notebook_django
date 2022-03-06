from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from notes.models import Notes

@login_required(login_url='/signin')
def dashboard(request):
    notes = Notes.objects.filter(user=request.user)
    past_notes = Notes.objects.order_by('-date')

    print(notes)
    return render(request, "dashboard.html",{"notes":notes, "past_notes":past_notes})

@login_required(login_url='/signin')
def add_notes(request):
    if request.method=="POST":
        title=request.POST.get('title')
        notes=request.POST.get('description')
        note = Notes(title=title, notes=notes, user=request.user)
        note.save()                             
        messages.add_message(request, messages.SUCCESS, 'Saved')
        return redirect(dashboard)
    else:
        return render(request, "add_notes.html")

@login_required(login_url='/signin')
def update_notes(request, id):
    if request.method=="POST":
        title=request.POST.get('title')
        notes=request.POST.get('description')

        note = Notes.objects.get(id=id)
        note.title=title
        note.notes=notes
        note.user=request.user
        note.save()         
       
        messages.add_message(request, messages.SUCCESS, 'Updated successfully')
        return redirect(dashboard)

    else:
        notes = Notes.objects.get(id=id)
        return render(request, "update_notes.html", {"notes":notes})                    

@login_required(login_url='/signin')
def notes(request, id):
        notes = Notes.objects.get(user=request.user, id=id)
        return render(request, "notes.html", {"notes":notes})

@login_required(login_url='/signin')
def delete_notes(request, id):
        notes = Notes.objects.get(id=id)
        notes.delete()
        messages.add_message(request, messages.SUCCESS, 'Deleted successfully')
        return redirect(dashboard)


