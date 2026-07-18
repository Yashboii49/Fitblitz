import os
import django
from datetime import timedelta
from django.utils import timezone

# Set up the Django environment so the script can talk to your database
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'new_one.settings')
django.setup()

from django.contrib.auth.models import User
from workouts.models import Exercise, Workout, WorkoutSet

def seed_data():
    print("Clearing old data...")
    Workout.objects.all().delete()
    Exercise.objects.all().delete()

    print("Fetching dummy user...")
    user = User.objects.first()
    if not user:
        print("Error: No user found. Did you run createsuperuser?")
        return

    print("Creating Bench Press...")
    bench_press = Exercise.objects.create(name="Bench Press", target_muscle="Chest")

    print("Simulating 5 weeks of progressive overload...")
    base_date = timezone.now() - timedelta(days=35)
    starting_weight = 135.0

    # Create 10 workouts over the last 35 days
    for i in range(10):
        workout = Workout.objects.create(
            user=user,
            date=base_date + timedelta(days=i*3)
        )
        
        # User gets slightly stronger each session (adding 2.5 lbs)
        current_weight = starting_weight + (i * 2.5) 
        
        # Log 3 sets of 10 reps for each workout
        for _ in range(3):
            WorkoutSet.objects.create(
                workout=workout,
                exercise=bench_press,
                weight=current_weight,
                reps=10,
                rpe=8
            )
            
    print("✅ Successfully seeded 10 workouts and 30 sets for Bench Press!")

if __name__ == '__main__':
    seed_data()