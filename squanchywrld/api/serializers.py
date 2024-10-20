from rest_framework import serializers
from .models import Game, Goal

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'  # Inclui todos os campos do modelo

class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = '__all__'  # Inclui todos os campos do modelo
