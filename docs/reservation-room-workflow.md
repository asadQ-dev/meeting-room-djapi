# 🚀 Runbook: Project Initialization & Configuration

This guide tracks the explicit execution layout needed to set up your directory, dependencies, and baseline framework code.

---

## 🧭 Step 1: Environment & Package Installation

* [x] **[Objective 1]** Run `python3 -m venv venv` in your terminal to initialize your project's isolated environment container.
* [x] **[Task]** Always activate your virtual environment (`source venv/bin/activate` on Linux) *before* installing packages or running commands, ensuring you are working inside the correct sandbox.
* [x] **[Objective 2]** Create your main project folder and navigate inside it using your terminal. *(Completed out-of-order by creating the repository directory first, which works perfectly).*
* [x] **[Objective 3]** Install the required core web packages inside your activated virtual environment:
  ```bash
  pip install django djangorestframework
  ```

---

## 🧭 Step 2: Scaffolding the System Layout

* [x] **[Objective 4]** Generate the master configuration controller and management script:
  ```bash
  django-admin startproject config .
  ```
* 💡 **[Fact]** The period `.` at the end of the `startproject` command forces Django to place the master setup files directly into your current folder instead of nesting a folder inside another folder. It also creates `manage.py`, your primary tool for executing terminal commands.
* [x] **[Objective 5]** Generate a self-contained module (an "App") specifically for your project features:
  ```bash
  python manage.py startapp reservations
  ```
* 💡 **[Fact]** Django divides projects into distinct structural "apps". Running this command generates a new `reservations/` directory containing dedicated files like `models.py`, `views.py`, and `admin.py`.

---

## 🧭 Step 3: Registering the Architecture

* [x] **[Objective 6]** Open `config/settings.py` in your text editor, find the `INSTALLED_APPS` array, and manually add `"rest_framework"` and `"reservations"` to the list:
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
* 📋 **[Task]** Always register new apps in `settings.py` immediately after creation. If an app is omitted from this list, Django will completely ignore its database instructions when you attempt to run migrations.

---

## 🧭 Step 4: Preparing the Serializer Component

* [x] **[Objective 7]** Create a brand-new, empty file named `serializers.py` directly inside your `reservations/` directory.
* 💡 **[Fact]** Standard Django does not ship with a `serializers.py` file by default. This is an explicit architectural component provided by the third-party *Django REST Framework (DRF)* library to clean and translate your web data.

---

## 🧭 Step 5: Defining the Database Models

* [x] **[Objective 8]** Open `reservations/models.py` in your text editor and write your database table blueprints using standard Python classes containing the `Room`, `Booking`, and `__str__` layout definitions.
* 💡 **[Fact]** Subclassing `models.Model` tells Django to treat a standard Python class as a database schema definition. 
* 💡 **[Fact]** The `on_delete=models.CASCADE` rule is a crucial relational safeguard. It tells the database that if a specific **Room** is completely deleted from the system, it must automatically find and delete all associated **Booking** allocations linked to that room to prevent orphaned data corruption.

---

## 🧭 Step 6: Executing Database Blueprints

* [x] **[Objective 9]** Run the tracking layout command in your terminal to have Django scan your new `models.py` changes and draft a blueprint file:
  ```bash
  python manage.py makemigrations
  ```

---

## 🧭 Step 7: Finalizing Database Tables

* [x] **[Objective 10]** Execute the layout blueprint to permanently construct the physical tables inside your database system:
  ```bash
  python manage.py migrate
  ```
* 📋 **[Task]** Always execute these two database migration commands sequentially (`makemigrations` then `migrate`) immediately after modifying code in `models.py`. Failing to execute them will cause your local server to crash with database missing errors when handling requests.

---

## 🧭 Step 8: Implementing Serializer Logic

* [ ] **[Objective 11]** Populate your empty `reservations/serializers.py` file with the core ModelSerializer classes mapping to the Room and Booking fields.
* [ ] **[Objective 12]** Write a custom `validate()` method inside the BookingSerializer class to implement the Date Order check and prevent time-interval overlaps.
* 💡 **[Fact]** Serializers convert raw incoming HTTP text parameters (JSON strings) into native Python dictionaries while validating data constraints before it hits your active models.

---

## 🧭 Step 9: Constructing the API Views

* [ ] **[Objective 13]** Open `reservations/views.py` and implement ModelViewSets or generic APIViews to process incoming web actions for creating and retrieving database entries.
* 💡 **[Fact]** Views act as the controller brain for inbound actions. They receive user requests, execute query searches via the database ORM, and deliver response schemas.

---

## 🧭 Step 10: Mapping the API Routing Network

* [ ] **[Objective 14]** Establish endpoint pathways inside a new `reservations/urls.py` file.
* [ ] **[Objective 15]** Link the reservation routes into the primary routing matrix located at `config/urls.py`.
* 💡 **[Fact]** The main URL router maps web entry endpoints (like `/bookings`) straight to the appropriate View controller logic blocks.

---

## 🎯 Master Progress Roadmap
* [x] 1. Environment: Create & activate venv.
* [x] 2. Install: pip install django djangorestframework.
* [x] 3. Scaffold: Run startproject and startapp commands.
* [x] 4. Register: Add "rest_framework" and "reservations" to settings.py.
* [x] 5. Models: Define Room and Booking tables in models.py.
* [x] 6. Track Plan: Run makemigrations in the terminal sandbox.
* [x] 7. Migrate: Execute migrate to physically construct tables.
* [ ] 8. Serializers Structure: Map models to base classes inside serializers.py.
* [ ] 9. Custom Validation: Code time-overlap checks inside serializers.py.
* [ ] 10. View Endpoints: Configure request controllers inside views.py.
* [ ] 11. App Routing: Define target application endpoints in reservations/urls.py.
* [ ] 12. Main Routing: Wire app entry gateways into config/urls.py.