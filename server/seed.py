from datetime import date
from app import app
from models import db, Exercise, Workout, WorkoutExercise 

with app.app_context():
    db.create_all()

    exercise1 = Exercise(
        name="Push-ups",
        category="Strength",
        equipment_needed=False
    )

    exercise2 = Exercise(
        name="Treadmill Running",
        category="Cardio",
        equipment_needed=True
    )

    db.session.add(exercise1)
    db.session.add(exercise2)
    db.session.commit()

    workout1 = Workout(
        date=date(2026, 10, 24),
        duration_minutes=30,
        notes="My first workout"
    )

    db.session.add(workout1)
    db.session.commit()

    workout_exercise1 = WorkoutExercise(
        workout_id=workout1.id,
        exercise_id=exercise1.id,
        reps=10,
        sets=3,
        duration_seconds=0
    )

    db.session.add(workout_exercise1)
    db.session.commit()

    workout_exercise2 = WorkoutExercise(
        workout_id=workout1.id,
        exercise_id=exercise2.id,
        reps=1,
        sets=1,
        duration_seconds=600
    )

    db.session.add(workout_exercise2)
    db.session.commit()
