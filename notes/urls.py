from unicodedata import name
from django.urls import path
from django.contrib import admin
from django.urls.conf import include

from notes.views.notes import add_notes, delete_notes, notes, update_notes
from .views.auth import home, signup, signin, dashboard, resetpassword, signout

urlpatterns = [
    path('', home, name="home"),
    path('dashboard', dashboard, name="dashboard"),
    path('signup', signup, name="signup"),
    path('signin', signin, name="signin"),
     path('signout', signout, name="signout"),
    path('resetpassword', resetpassword, name="resetpassword"),

    path('add_notes', add_notes, name="add_notes"),
    path('notes/<id>', notes, name="notes"),
    path('update_notes/<id>', update_notes, name="update_notes"),
    path('delete_notes/<id>', delete_notes, name="delete_notes"),



]
