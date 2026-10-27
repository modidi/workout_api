from marshmallow import Schema,fields, validates, ValidationError

class ExerciseSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    category = fields.String(required=True)
    equipment_needed = fields.Boolean(required=True)

    workout_exercises = fields.Nested(
        "WorkoutExerciseSchema",
        many=True,
        dump_only=True
    )

    @validates("name")
    def validate_name(self, value):
        if not value or not value.strip():
            raise ValidationError("Exercise name cannot be empty")
            
class WorkoutSchema(Schema):
    id = fields.Integer(dump_only=True)
    date = fields.Date(required=True)
    duration_minutes = fields.Integer(required=True)
    notes = fields.String(required=False, allow_none=True)
    workout_exercises = fields.Nested("WorkoutExerciseSchema", many=True, dump_only=True)

    @validates("duration_minutes")
    def validate_duration(self, value):
        if value <= 0:
            raise ValidationError("Workout duration must be greater than zero")

class WorkoutExerciseSchema(Schema):
    workout_id = fields.Integer(required=True)
    exercise_id = fields.Integer(required=True)
    exercise = fields.Nested("ExerciseSchema", exclude=("workout_exercises",),dump_only=True)
    reps = fields.Integer(required=True)
    sets = fields.Integer(required=True)
    duration_seconds = fields.Integer(required=True)

    @validates("reps")
    def validate_reps(self, value):
        if value <= 0:
            raise ValidationError("Reps must be greater than zero")

    @validates("sets")
    def validate_sets(self, value):
        if value <= 0:
            raise ValidationError("Sets must be greater than zero")

    @validates("duration_seconds")
    def validate_duration(self, value):
        if value < 0:
            raise ValidationError("Duration must be greater than zero")
