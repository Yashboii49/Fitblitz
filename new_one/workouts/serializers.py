from rest_framework import serializers
from .models import Exercise, Workout, WorkoutSet

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['id', 'name', 'target_muscle']

class WorkoutSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutSet
        # We include the ID so the mobile app can edit/delete specific sets later
        fields = ['id', 'workout', 'exercise', 'weight', 'reps', 'rpe']

class WorkoutSerializer(serializers.ModelSerializer):
    # This automatically fetches all the sets associated with this workout
    # so the mobile app gets the full picture in one API call.
    sets = WorkoutSetSerializer(many=True, read_only=True)

    class Meta:
        model = Workout
        fields = ['id', 'user', 'date', 'notes', 'biometrics', 'sets']
        # We make user read-only because the backend will automatically 
        # figure out who is logging the workout based on their login token.
        read_only_fields = ['user']