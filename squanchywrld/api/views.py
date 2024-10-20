from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Game, Goal
from .serializers import GameSerializer, GoalSerializer

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GoalViewSet(viewsets.ModelViewSet):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer
