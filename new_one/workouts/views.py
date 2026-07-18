from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny # <-- Changed this
from rest_framework.response import Response
from django.contrib.auth.models import User # <-- Added this to get the dummy user
from .models import Exercise, Workout, WorkoutSet
from .serializers import ExerciseSerializer, WorkoutSerializer, WorkoutSetSerializer
from .ml_service import predict_next_weight

class ExerciseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [AllowAny] # <-- Bypass

class WorkoutViewSet(viewsets.ModelViewSet):
    serializer_class = WorkoutSerializer
    permission_classes = [AllowAny] # <-- Bypass

    def get_queryset(self):
        # TEMPORARY BYPASS: Pretend the requester is the first user
        dummy_user = User.objects.first()
        return Workout.objects.filter(user=dummy_user).order_by('-date')

    def perform_create(self, serializer):
        # Attach the first user to any newly created workouts
        dummy_user = User.objects.first()
        serializer.save(user=dummy_user)

class WorkoutSetViewSet(viewsets.ModelViewSet):
    serializer_class = WorkoutSetSerializer
    permission_classes = [AllowAny] # <-- Bypass

    def get_queryset(self):
        dummy_user = User.objects.first()
        return WorkoutSet.objects.filter(workout__user=dummy_user)


@api_view(['GET'])
@permission_classes([AllowAny]) # <-- Bypass
def get_workout_suggestion(request, exercise_id):
    target_reps = int(request.GET.get('reps', 10)) 
    
    # Use our dummy user instead of requiring a login
    dummy_user = User.objects.first() 
    
    prediction = predict_next_weight(dummy_user, exercise_id, target_reps)
    return Response(prediction)