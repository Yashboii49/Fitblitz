from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExerciseViewSet, WorkoutViewSet, WorkoutSetViewSet, get_workout_suggestion

router = DefaultRouter()
router.register(r'exercises', ExerciseViewSet)
router.register(r'workouts', WorkoutViewSet, basename='workout')
router.register(r'sets', WorkoutSetViewSet, basename='workoutset')

urlpatterns = [
    path('', include(router.urls)),
    path('suggest/<int:exercise_id>/', get_workout_suggestion, name='workout-suggestion'),
]