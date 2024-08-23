from django.db import models
import string
import random


# Models represent tables with their rows and columns (similar to Laravel).
# Django lets us create a model instead of a table and all operations done on the models
# will be interpreted as database operations. Similar to Laravel, Models are an abstraction
# from the database.

# we need to run `python manage.py makemigrations` and this will create a database migration
# based on the below model (and any new model we created after the last run of makemigrations)

def generate_unique_code():
    length = 6

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))

        # make sure the code is unique => no room has this code yet
        if Room.objects.filter(code=code).count() == 0:
            return code


# Create your models here.
class Room(models.Model):
    # code to identify a room: we put the constraints like we do in any migration
    code = models.CharField(max_length=8, default="", unique=True)
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(default=False)
    votes_to_skip = models.IntegerField(default=1)
    # automatically add the current date time for this field
    created_at = models.DateTimeField(auto_now_add=True)
