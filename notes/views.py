from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password
from notes.models import Users
import random,string
from .email import sendpassword

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
            messages.add_message(request, messages.SUCCESS, 'New password has been sent to your email!')
            return redirect(signin)

    else:
        return render(request, "auth/resetpassword.html")

def dashboard(request):
    return render(request, "dashboard.html")



            
           