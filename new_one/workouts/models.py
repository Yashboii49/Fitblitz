from django.db import models
from django.contrib.auth.models import User
from django.db.models import JSONField

# 1. Exercise MUST come first
class Exercise(models.Model):
    name = models.CharField(max_length=100)
    target_muscle = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

# 2. Workout MUST come second
class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workouts')
    date = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True)
    biometrics = JSONField(default=dict, blank=True) 

    def __str__(self):
        return f"{self.user.username} - {self.date}"

# 3. WorkoutSet MUST come last (so it can properly link to Workout and Exercise)
class WorkoutSet(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='sets')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    weight = models.FloatField(help_text="Weight in lbs/kg")
    reps = models.IntegerField()
    rpe = models.IntegerField(null=True, blank=True) 

    class Meta:
        indexes = [
            models.Index(fields=['workout', 'exercise']),
        ]

    def __str__(self):
        return f"{self.exercise.name}: {self.weight} x {self.reps}"