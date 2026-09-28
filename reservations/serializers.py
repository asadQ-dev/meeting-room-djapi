
from rest_framework import serializers  # type: ignore[reportMissingImports]
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
        start = data.get('start_time', getattr(self.instance, 'start_time', None))
        end = data.get('end_time', getattr(self.instance, 'end_time', None))
        room = data.get('room', getattr(self.instance, 'room', None))

        if start >= end:
            raise serializers.ValidationError("End time must be after start time.")

        overlapping = Booking.objects.filter(
            room=room,
            start_time__lt=end,
            end_time__gt=start,
        )
        if self.instance:
            overlapping = overlapping.exclude(pk=self.instance.pk)

        if overlapping.exists():
            raise serializers.ValidationError(
                "This room is already booked for the specified time interval."
            )

        return data
