# Workout API

## Description

Workout API is a Flask REST API that helps personal trainers manage workouts and exercises.

The API allows users to:
- View all workouts and retrieve a single workout.
- Create and delete workouts.
- View all exercises and retrieve a single exercise.
- Create and delete exercises.
- Add exercises to workouts with the number of repetitions, sets, and duration.

The application uses Flask, Flask-SQLAlchemy, SQLite, and Marshmallow for database management, data serialization, and validation.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/modidi/workout_api.git
cd workout_api
```

### 2. Install dependencies

```bash
pipenv install
```

### 3. Activate the virtual environment

```bash
pipenv shell
```

### 4. Set up the database

Run the database migrations:

```bash
pipenv run flask --app server/app.py db upgrade
```

### 5. Seed the database

```bash
pipenv run python server/seed.py
```

### 6. Run the application

```bash
cd server
pipenv run python app.py
```

The API will be available at:

`http://127.0.0.1:5555`

## API Endpoints

### Workouts

| Method | Endpoint | Description |
|---|---|---|
| GET | `/workouts` | Retrieve all workouts |
| GET | `/workouts/<id>` | Retrieve one workout with its associated exercises |
| POST | `/workouts` | Create a workout |
| DELETE | `/workouts/<id>` | Delete a workout |

### Exercises

| Method | Endpoint | Description |
|---|---|---|
| GET | `/exercises` | Retrieve all exercises |
| GET | `/exercises/<id>` | Retrieve one exercise |
| POST | `/exercises` | Create an exercise |
| DELETE | `/exercises/<id>` | Delete an exercise |

### Workout Exercises

| Method | Endpoint | Description |
|---|---|---|
| POST | `/workouts/<workout_id>/exercises/<exercise_id>/workout_exercises` | Add an exercise to a workout |

### Example Request Bodies

#### Create a workout

```json
{
  "date": "2026-10-25",
  "duration_minutes": 30,
  "notes": "My first workout"
}
```

#### Create an exercise

```json
{
  "name": "Push-ups",
  "category": "Strength",
  "equipment_needed": false
}
```

#### Add an exercise to a workout

Send a `POST` request to `/workouts/1/exercises/1/workout_exercises` with:

```json
{
  "reps": 10,
  "sets": 3,
  "duration_seconds": 0
}
```

Replace the IDs in the URL with the IDs of the workout and exercise you want to connect.