from unicodedata import name
from django.urls import path
from django.contrib import admin
from django.urls.conf import include
from .views import home, signup, signin, dashboard

urlpatterns = [
    path('', home, name="home"),
    path('dashboard', dashboard, name="dashboard"),
    path('signup', signup, name="signup"),
    path('signin', signin, name="signin"),

]
