from unicodedata import name
from django.urls import path
from django.contrib import admin
from django.urls.conf import include
from .views import home, signup, signin, dashboard, resetpassword, signout

urlpatterns = [
    path('', home, name="home"),
    path('dashboard', dashboard, name="dashboard"),
    path('signup', signup, name="signup"),
    path('signin', signin, name="signin"),
     path('signout', signout, name="signout"),
    path('resetpassword', resetpassword, name="resetpassword"),

    

]
