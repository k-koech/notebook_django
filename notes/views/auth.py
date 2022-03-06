from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password
from notes.models import Notes, Users
import random,string
from django.contrib.auth.decorators import login_required
from notes.views.notes import dashboard
from ..email import sendpassword

# Create your views here.
def home(request):
    return render(request, "index.html")

def signup(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('pass')
        re_password=request.POST.get('re_pass')

        username_exist=Users.objects.filter(username=username).count()
        email_exist=Users.objects.filter(email=email).count()

        if email_exist>0:
            messages.add_message(request, messages.ERROR, 'Email Exists!')
            return redirect(signup)
        
        elif len(username)<3:
            messages.add_message(request, messages.ERROR, 'Username should have atleast 3 characters!')
            return redirect(signup)

        elif username_exist>0:
            messages.add_message(request, messages.ERROR, 'Username Exists!')
            return redirect(signup)

        elif len(password)<4:
            messages.add_message(request, messages.ERROR, 'Password is too short')
            return redirect(signup)

        elif password!=re_password:
            messages.add_message(request, messages.ERROR, 'Password do not match!')
            return redirect(signup)
        else:
            user = Users(username=username, email=email,password=make_password(password))
            user.save()                             
            messages.add_message(request, messages.SUCCESS, 'Registered successfully')
            return redirect(signin)
       

    else:
        return render(request, "auth/signup.html")

def signin(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('pass')

        user= authenticate(email=email, password=password)

        if user is not None:
            login(request,user )
            messages.add_message(request, messages.INFO, 'Successfully logged in!')
            return redirect(dashboard)
 
        else:
            messages.add_message(request, messages.ERROR, 'Credentials do not match our record!')
            return redirect(signin)
    

    else:
        return render(request, "auth/signin.html")

def signout(request):
    logout(request)
    messages.add_message(request, messages.INFO, 'Successfully logged out!')
    return redirect(signin)
 
@login_required(login_url='/signin')
def resetpassword(request):
    if request.method=="POST":
        email=request.POST.get('email')
        generated_password=str(''.join(random.choices(string.ascii_uppercase + string.digits, k = 10)))

        email_exist=Users.objects.filter(email=email).count()
        if email_exist==0:
            messages.add_message(request, messages.ERROR, 'Email do not exist!')
            return redirect(resetpassword)
        else:
            username = Users.objects.get(email=email).username
            sendpassword(username,generated_password,email)
            user = Users.objects.get(email = email)
            user.password = make_password(generated_password)
            user.save()
            messages.add_message(request, messages.SUCCESS, 'New password has been sent to your email!')
            return redirect(signin)

    else:
        return render(request, "auth/resetpassword.html")

"""PROFILE"""
@login_required(login_url='/signin')
def profile(request):
    if request.method=="POST":
         if 'user' in request.POST:
            if 'update_password' == request.POST.get('user'): 
                old_password=request.POST.get('old_password')
                new_password=request.POST.get('new_password')
                re_password=request.POST.get('re_password')
                
                user = Users.objects.get(id=request.user.id)
                if user.check_password('{}'.format(old_password)) == False:
                    messages.add_message(request,messages.ERROR,"Old password is wrong!")
                    return redirect(profile)
                elif len(new_password)<4 or len(re_password)<4:
                    messages.add_message(request,messages.ERROR,"Password too short!")
                    return redirect(profile)
                elif new_password!=re_password:
                    messages.add_message(request,messages.ERROR,"Password doesn't match!")
                    return redirect(profile)
                else:
                    user = Users.objects.get(id=request.user.id)
                    user.password = make_password(new_password)
                    user.save()
                    messages.add_message(request, messages.SUCCESS, 'Password updated successfully!')
                    return redirect(profile)

    else:
        count_notes = Notes.objects.filter(id=request.user.id).count()
        return render(request, "profile.html", {"count_notes":count_notes})

            
           