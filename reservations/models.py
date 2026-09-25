from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    booked_by = models.CharField(max_length=100) 
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.room.name} booking from {self.start_time} to {self.end_time}"
