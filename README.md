# Meeting Room DJAPI

## Project Overview

A Django REST API for managing meeting room bookings with time conflict detection to prevent double-booking.

## Features

- Room management (create, view, update, delete)
- Booking management with time conflict detection
- RESTful API endpoints for all operations
- Time-based booking validation to prevent overlaps

## Getting Started

### Prerequisites

- Python 3.8+
- Django 4.0+
- Django REST Framework
- SQLite (for development)

### Installation

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment
4. Install dependencies: `pip install -r requirements.txt` (if exists)
5. Run migrations: `python manage.py migrate`

### Setup

1. Create a superuser: `python manage.py createsuperuser`
2. Start the development server: `python manage.py runserver`
3. Access the admin interface at http://localhost:8000/admin/

## Usage

The API provides endpoints for managing rooms and bookings:
- `/api/rooms/` - List and create rooms
- `/api/bookings/` - List and create bookings
- `/api/rooms/{id}/` - Retrieve, update, or delete specific room
- `/api/bookings/{id}/` - Retrieve, update, or delete specific booking

## API Endpoints

[Placeholder for API endpoint documentation]

## Models

### Room Model

Represents meeting rooms available for booking:
- `name` (CharField): Name of the room
- `capacity` (IntegerField): Maximum number of people the room can hold

### Booking Model

Represents booking reservations:
- `room` (ForeignKey): Reference to the Room model
- `booked_by` (CharField): Name/identifier of the person who made the booking
- `start_time` (DateTimeField): Start time of the booking
- `end_time` (DateTimeField): End time of the booking

## Contributing

[Placeholder for contribution guidelines]

## License

[Placeholder for license information]

## Acknowledgments

[Placeholder for acknowledgments]