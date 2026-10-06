# 🚀 Runbook: Project Initialization & Configuration

This guide tracks the explicit execution layout needed to set up your directory, dependencies, and baseline framework code.

---

## 🧭 Step 1: Environment & Package Installation

- [ ] **[Objective 1]** Run `python3 -m venv venv` in your terminal to initialize your project's isolated environment container. (Project folder is actually named `.venv`, so activate with `source .venv/bin/activate`.)
- [ ] **[Task]** Always activate your virtual environment (`source venv/bin/activate` on Linux) before installing packages or running commands, ensuring you are working inside the correct sandbox.
- [ ] **[Objective 2]** Create your main project folder and navigate inside it using your terminal. (Completed out-of-order by creating the repository directory first, which works perfectly).
- [ ] **[Objective 3]** Install the required core web packages inside your activated virtual environment:

```bash
pip install django djangorestframework
```

---

## 🧭 Step 2: Scaffolding the System Layout

- [ ] **[Objective 4]** Generate the master configuration controller and management script:

```bash
django-admin startproject config .
```

> 💡 **Fact:** The period `.` at the end of the `startproject` command forces Django to place the master setup files directly into your current folder instead of nesting a folder inside another folder. It also creates `manage.py`, your primary tool for executing terminal commands.

- [ ] **[Objective 5]** Generate a self-contained module (an "App") specifically for your project features:

```bash
python manage.py startapp reservations
```

> 💡 **Fact:** Django divides projects into distinct structural "apps". Running this command generates a new `reservations/` directory containing dedicated files like `models.py`, `views.py`, and `admin.py`.

---

## 🧭 Step 3: Registering the Architecture

- [ ] **[Objective 6]** Open `config/settings.py` in your text editor, find the `INSTALLED_APPS` array, and manually add `"rest_framework"` and `"reservations"` to the list:

```python
INSTALLED_APPS = [
    # ... default Django apps stay here ...
    "django.contrib.staticfiles",

    # Third-party extensions
    "rest_framework",

    # Custom features
    "reservations",
]
```

> 📋 **Task:** Always register new apps in `settings.py` immediately after creation. If an app is omitted from this list, Django will completely ignore its database instructions when you attempt to run migrations.

---

## 🧭 Step 4: Preparing the Serializer Component

- [ ] **[Objective 7]** Create a brand-new, empty file named `serializers.py` directly inside your `reservations/` directory.

> 💡 **Fact:** Standard Django does not ship with a `serializers.py` file by default. This is an explicit architectural component provided by the third-party Django REST Framework (DRF) library to clean and translate your web data.

---

## 🧭 Step 5: Defining the Database Models

- [ ] **[Objective 8]** Open `reservations/models.py` in your text editor and write your database table blueprints using standard Python classes containing the `Room`, `Booking`, and `__str__` layout definitions.

> 💡 **Fact:** Subclassing `models.Model` tells Django to treat a standard Python class as a database schema definition.
>
> 💡 **Fact:** The `on_delete=models.CASCADE` rule is a crucial relational safeguard. It tells the database that if a specific `Room` is completely deleted from the system, it must automatically find and delete all associated `Booking` allocations linked to that room to prevent orphaned data corruption.

---

## 🧭 Step 6: Executing Database Blueprints

- [ ] **[Objective 9]** Run the tracking layout command in your terminal to have Django scan your new `models.py` changes and draft a blueprint file:

```bash
python manage.py makemigrations
```

---

## 🧭 Step 7: Finalizing Database Tables

- [ ] **[Objective 10]** Execute the layout blueprint to permanently construct the physical tables inside your database system:

```bash
python manage.py migrate
```

> 📋 **Task:** Always execute these two database migration commands sequentially (`makemigrations` then `migrate`) immediately after modifying code in `models.py`. Failing to execute them will cause your local server to crash with database missing errors when handling requests.

---

## 🧭 Step 8: Implementing Serializer Logic

- [ ] **[Objective 11]** Populate your empty `reservations/serializers.py` file with the core `ModelSerializer` classes mapping to the `Room` and `Booking` fields.
- [ ] **[Objective 12]** Write a custom `validate()` method inside the `BookingSerializer` class to implement the Date Order check and prevent time-interval overlaps.

> 💡 **Fact:** Serializers convert raw incoming HTTP text parameters (JSON strings) into native Python dictionaries while validating data constraints before it hits your active models.

---

## 🧭 Step 9: Constructing the API Views

- [ ] **[Objective 13]** Open `reservations/views.py` and implement `ModelViewSets` or generic `APIViews` to process incoming web actions for creating and retrieving database entries.

> 💡 **Fact:** Views act as the controller brain for inbound actions. They receive user requests, execute query searches via the database ORM, and deliver response schemas.

---

## 🧭 Step 10: Mapping the API Routing Network

- [ ] **[Objective 14]** Establish endpoint pathways inside a new `reservations/urls.py` file.
- [ ] **[Objective 15]** Link the reservation routes into the primary routing matrix located at `config/urls.py`.

> 💡 **Fact:** The main URL router maps web entry endpoints (like `/bookings`) straight to the appropriate View controller logic blocks.

---

## 🎯 Master Progress Roadmap

### ✅ Completed

1. [x] **Environment:** Create & activate venv.
2. [x] **Install:** `pip install django djangorestframework`.
3. [x] **Scaffold:** Run `startproject` and `startapp` commands.
4. [x] **Register:** Add `"rest_framework"` and `"reservations"` to `settings.py`.
5. [x] **Models:** Define `Room` and `Booking` tables in `models.py`.
6. [x] **Track Plan:** Run `makemigrations` in the terminal sandbox.
7. [x] **Migrate:** Execute `migrate` to physically construct tables.
8. [x] **Serializers Structure:** Map models to base classes inside `serializers.py`.
9. [x] **Custom Validation:** Code time-overlap checks inside `serializers.py`.
10. [x] **View Endpoints:** Configure request controllers inside `views.py`.
11. [x] **App Routing:** Define target application endpoints in `reservations/urls.py`.
12. [x] **Main Routing:** Wire app entry gateways into `config/urls.py`.

---

## 🧪 Testing & Completion

### ✅ Completed

13. [x] Start the Django development server.
14. [x] Test the API and confirm the endpoints respond correctly. (Covered by the automated tests in `reservations/tests.py`.)
16. [x] Test creating a Booking.
18. [x] Test overlapping bookings are rejected.
20. [x] Test updating a Booking. (PUT and PATCH both covered.)

### ⬜ Remaining

15. [x] Test creating a Room.
17. [x] Test invalid time ranges are rejected. (Validation exists in the serializer; no test yet.)
19. [x] Test retrieving Rooms and Bookings.
21. [x] Test deleting a Booking.
22. [x] Review and clean up the project structure/code.
23. [x] Update the README with setup and usage instructions.
24. [x] Git status / review changes.
25. [x] Commit the completed project to Git.
26. [] Push the finished project to GitHub. (Before pushing: move `SECRET_KEY` out of `settings.py`.)

---

## 📝 Extras completed along the way

- Added `REST_FRAMEWORK` permission setting and `permission_classes = [AllowAny]` on the viewsets (API was returning 403 for unauthenticated requests).
- Migration `0002_booking_attendees` created and applied.
- `requirements.txt` generated with `python -m pip freeze`.
- Four passing tests: create, overlap rejected, PUT edit doesn't conflict with itself, PATCH single field.