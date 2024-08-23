from django.urls import path
from .views import main

urlpatterns = [
    # point the blank url to the main function imported from views
    path('home', main)
]