from django.db import models


class Booking(models.Model):
    ROOM_TYPES = [
        ('single', 'Single Room'),
        ('double', 'Double Room'),
        ('suite', 'Suite'),
        ('family', 'Family Room'),
    ]
   
    name = models.CharField(max_length=100)
    email = models.EmailField()
    checkin = models.DateField()
    checkout = models.DateField()
    roomtype = models.CharField(max_length=20, choices=ROOM_TYPES)
    guests = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} ({self.roomtype}) from {self.checkin} to {self.checkout}"
 
 