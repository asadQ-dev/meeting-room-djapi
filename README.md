# meeting-room-djapi

A basic Django + Django REST Framework project for managing meeting rooms and room bookings.

## Status

This repository appears to be an early draft/prototype. Core models and serializers exist, while API views, routing, and tests are still incomplete.

## Project Goals

- Manage meeting rooms
- Create room bookings
- Prevent overlapping bookings for the same room
- Provide API endpoints for room and booking operations

## Tech Stack

- Python
- Django
- Django REST Framework
- SQLite (default local database)

## Current Features

- `Room` model with:
  - `name`
  - `capacity`
- `Booking` model with:
  - `room`
  - `booked_by`
  - `start_time`
  - `end_time`
- Serializer validation to:
  - ensure `end_time` is after `start_time`
  - block overlapping bookings for the same room

## Repository Structure

```text
meeting-room-djapi/
├── config/                 # Django project configuration
├── docs/                   # Project notes / workflow docs
├── reservations/           # Main app for rooms and bookings
├── manage.py               # Django management entry point
└── README.md
```

## Getting Started

### 1. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install django djangorestframework
```

> Placeholder: add a `requirements.txt` or lockfile if dependency management is added later.

### 3. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Run the development server

```bash
python manage.py runserver
```

### 5. Open the app

- Django admin: `http://127.0.0.1:8000/admin/`
- API base path: not implemented yet

## Available Commands

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
python manage.py test
```

## Data Model Overview

### Room

- `name`: room name
- `capacity`: room capacity

### Booking

- `room`: linked room
- `booked_by`: person who booked the room
- `start_time`: booking start datetime
- `end_time`: booking end datetime

## API

Current API implementation status:

- Models: done
- Serializers: done
- Views: draft / incomplete
- URL routing: draft / incomplete
- Tests: placeholder / incomplete

### Proposed Endpoints

> Placeholder: these are draft route ideas and are not implemented yet.

- `GET /rooms/`
- `POST /rooms/`
- `GET /bookings/`
- `POST /bookings/`

## Documentation

- Workflow notes: `/docs/reservation-room-workflow.md`

## Configuration Notes

- Database: SQLite by default
- Email backend: console backend
- Debug mode: enabled in current settings

> Placeholder: add production configuration guidance before deployment.

## Testing

Current test coverage is minimal.

> Placeholder: document test strategy and add endpoint/model validation tests.

## Roadmap / TODO

- Implement booking and room API views
- Add app-level URL routing
- Register routes in the project URL config
- Add tests for model and serializer behavior
- Add authentication/permissions if needed
- Add deployment instructions

## Contributing

> Placeholder: add contribution guidelines, code style, and PR expectations.

## License

No license file is currently present in this repository.
