
from rest_framework import serializers
from .models import Room, Booking

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"

    def validate(self, data):
        if data['start_time'] >= data['end_time']:
            raise serializers.ValidationError("End time must be after start time.")

        room = data['room']
        overlapping = Booking.objects.filter(
            room=room,
            start_time__lt=data['end_time'],
            end_time__gt=data['start_time']
        )
        if overlapping.exists():
            raise serializers.ValidationError("This room is already booked for the specified time interval.")

        return data
