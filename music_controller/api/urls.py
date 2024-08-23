from django.urls import path
from .views import RoomView, RoomCreate

urlpatterns = [
    # point the blank url to the main function imported from views
    path('rooms/', RoomView.as_view()),
    path('rooms/create', RoomCreate.as_view())
]
