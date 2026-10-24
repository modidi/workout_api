from marshmallow import Schema,fields, validates, ValidationError

class ExerciseSchema(Schema):
    name = fields.String(required=True)
    category = fields.String(required=True)
    equipment_needed = fields.Boolean(required=True)

    @validates("name")
    def validate_name(self, value):
        if not value.strip():
            raise ValidationError("Exercise name cannot be empty")
            
class WorkoutSchema(Schema):
    date = fields.Date(required=True)
    duration_minutes = fields.Integer(required=True)
    notes = fields.String(required=False, allow_none=True)

    @validates("duration_minutes")
    def validate_duration(self, value):
        if value <= 0:
            raise ValidationError("Workout duration must be greater than zero")

class WorkoutExerciseSchema(Schema):
    workout_id = fields.Integer(required=True)
    exercise_id = fields.Integer(required=True)
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
            raise ValidationError("Duration cannot be negative")
