from .models import Room, Booking
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.response import Response

class BookingAPITestCase(APITestCase):
    def setUp(self):
        self.room = Room.objects.create(name="Conference Room", capacity=10)
        self.booking = Booking.objects.create(
            room=self.room,
            booked_by="John Doe",
            attendees=5,
            start_time="2024-06-01T10:00:00Z",
            end_time="2024-06-01T11:00:00Z"
        )
        self.booking_data = {
            "room": self.room.pk,
            "booked_by": "John Doe",
            "attendees": 5,
            "start_time": "2024-06-01T12:00:00Z",
            "end_time": "2024-06-01T13:00:00Z"
        }

    def test_create_booking(self):
        response: Response = self.client.post("/reservations/bookings/", self.booking_data, format="json")  # type: ignore[assignment]
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        assert response.data is not None
        self.assertEqual(response.data["room"], self.room.pk)
        self.assertEqual(response.data["booked_by"], "John Doe")
        self.assertEqual(response.data["attendees"], 5)
        self.assertEqual(response.data["start_time"], "2024-06-01T12:00:00Z")
        self.assertEqual(response.data["end_time"], "2024-06-01T13:00:00Z")
    def test_overlapping_booking_is_rejected(self):
        self.client.post("/reservations/bookings/", self.booking_data, format="json")  
        overlapping_booking_data = {
            "room": self.room.pk,
            "booked_by": "Jane Doe",
            "attendees": 3,
            "start_time": "2024-06-01T10:30:00Z",
            "end_time": "2024-06-01T11:30:00Z"
        }
        response: Response = self.client.post("/reservations/bookings/", overlapping_booking_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("This room is already booked for the specified time interval.", str(response.data))

    def test_editing_booking_does_not_conflict_with_itself(self):
        response: Response = self.client.post("/reservations/bookings/", self.booking_data, format="json")
        updated_booking_data = {
            "room": self.room.pk,
            "booked_by": "John Doe",
            "attendees": 5,
            "start_time": "2024-06-01T12:00:00Z",
            "end_time": "2024-06-01T13:00:00Z"
        }
        response: Response = self.client.put(f"/reservations/bookings/{response.data['id']}/", updated_booking_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["room"], self.room.pk)
        self.assertEqual(response.data["booked_by"], "John Doe")
        self.assertEqual(response.data["attendees"], 5)
        self.assertEqual(response.data["start_time"], "2024-06-01T12:00:00Z")
        self.assertEqual(response.data["end_time"], "2024-06-01T13:00:00Z")

    def test_patch_booking_field(self):
        patch_data = {
            "booked_by": "Someone Else"
        }
        response: Response = self.client.patch(f"/reservations/bookings/{self.booking.pk}/", patch_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["booked_by"], "Someone Else")