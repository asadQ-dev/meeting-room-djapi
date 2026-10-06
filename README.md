# Meeting Room DJAPI

A small Django REST Framework API for booking meeting rooms, built as a training project to solidify core Django/DRF architecture: models, migrations, serializers, viewsets, routers, and tests.

## Features

- CRUD for rooms and bookings via DRF `ModelViewSet`s and a `DefaultRouter`
- Server-side validation that rejects overlapping bookings for the same room
- Server-side validation that rejects bookings where `end_time` is before `start_time`
- Automated test suite (`reservations/tests.py`) covering creation, retrieval, update, delete, and conflict handling

## Tech Stack

- Python 3
- Django 6.1.1, Django REST Framework 3.18.1 (pinned in [requirements.txt](requirements.txt), along with `asgiref`, `sqlparse`, and `python-dotenv==1.2.4`)
- SQLite (default dev database)
- `python-dotenv` for loading environment variables from a `.env` file

## Project Structure

```
config/              # Django project: settings, root URLConf, WSGI/ASGI
reservations/         # App: models, serializers, views, urls, tests
docs/                 # Build/runbook notes from building this project
manage.py
requirements.txt
```

## Getting Started

### Prerequisites

- Python 3.11+ (any 3.x compatible with Django 6.1 should work)

### Installation

```bash
git clone https://github.com/asadQ-dev/meeting-room-djapi.git
cd meeting-room-djapi
python -m venv .venv
source .venv/bin/activate      # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Configuration

The app reads `DJANGO_SECRET_KEY` from the environment (via `python-dotenv`). Create a `.env` file in the project root:

```
DJANGO_SECRET_KEY=replace-with-a-long-random-string
```

### Database setup

```bash
python manage.py migrate
```

### Running the server

```bash
python manage.py runserver
```

Optionally create an admin user and use the Django admin at `http://localhost:8000/admin/`:

```bash
python manage.py createsuperuser
```

### Running tests

```bash
python manage.py test
```

## API Endpoints

All endpoints are mounted under `/reservations/` (see [config/urls.py](config/urls.py)) and registered through a DRF router (see [reservations/urls.py](reservations/urls.py)), so each resource gets the standard list/detail routes:

| Method | URL | Description |
|---|---|---|
| GET | `/reservations/rooms/` | List rooms |
| POST | `/reservations/rooms/` | Create a room |
| GET | `/reservations/rooms/{id}/` | Retrieve a room |
| PUT/PATCH | `/reservations/rooms/{id}/` | Update a room |
| DELETE | `/reservations/rooms/{id}/` | Delete a room |
| GET | `/reservations/bookings/` | List bookings |
| POST | `/reservations/bookings/` | Create a booking |
| GET | `/reservations/bookings/{id}/` | Retrieve a booking |
| PUT/PATCH | `/reservations/bookings/{id}/` | Update a booking |
| DELETE | `/reservations/bookings/{id}/` | Delete a booking |

### Example: create a booking

```bash
curl -X POST http://localhost:8000/reservations/bookings/ \
  -H "Content-Type: application/json" \
  -d '{
        "room": 1,
        "booked_by": "Jane Doe",
        "attendees": 4,
        "start_time": "2026-10-10T09:00:00Z",
        "end_time": "2026-10-10T10:00:00Z"
      }'
```

Booking creation/updates fail with `400 Bad Request` if `end_time` is not after `start_time`, or if the room is already booked for an overlapping interval.

## Models

### `Room`

| Field | Type | Notes |
|---|---|---|
| `name` | `CharField(max_length=100)` | |
| `capacity` | `IntegerField` | |

### `Booking`

| Field | Type | Notes |
|---|---|---|
| `room` | `ForeignKey(Room)` | `on_delete=CASCADE` — deleting a room deletes its bookings |
| `booked_by` | `CharField(max_length=100)` | optional, defaults to `"Unknown"` |
| `attendees` | `PositiveIntegerField` | optional, defaults to `1` |
| `start_time` | `DateTimeField` | |
| `end_time` | `DateTimeField` | |

## Notes on this being a learning project

- Permissions are set to `AllowAny` for all viewsets (see `REST_FRAMEWORK` in [config/settings.py](config/settings.py)) — there is no authentication, so this is not suitable to deploy as-is.
- `DEBUG = True` and `ALLOWED_HOSTS` is empty — fine for local development only.
- See [docs/reservation-room-workflow.md](docs/reservation-room-workflow.md) for the step-by-step build log of how this project was scaffolded, which is useful if you're following along to learn the same architecture.

## Potential Improvements

Things a production-grade version of this API would typically add:

- **Authentication & authorization** — replace `AllowAny` with token/session auth (DRF `TokenAuthentication` or JWT) and permission classes like `IsAuthenticated`, plus scoping bookings to the requesting user instead of a free-text `booked_by` field.
- **Pagination** — add `DEFAULT_PAGINATION_CLASS`/`PAGE_SIZE` to `REST_FRAMEWORK` settings so `rooms/` and `bookings/` list endpoints don't return unbounded result sets.
- **Filtering & search** — integrate `django-filter` to query bookings by `room`, date range, or `booked_by`.
- **Nested/readable serialization** — nest room details (name, capacity) inside booking responses instead of just the room id, and validate `attendees <= room.capacity`.
- **Environment-based settings** — split `settings.py` into base/dev/prod modules, set `DEBUG = False` and real `ALLOWED_HOSTS` for production.
- **Postgres support** — swap SQLite for Postgres via `DATABASE_URL`/`dj-database-url` for a deployable setup.
- **API documentation** — add `drf-spectacular` or `drf-yasg` for an OpenAPI schema and Swagger/Redoc UI.
- **CI** — run `python manage.py test` automatically on push via GitHub Actions.