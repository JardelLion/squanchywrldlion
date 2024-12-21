from rest_framework import serializers
from .models import Game, Performance, Moment, TeamScoreStats

class MomentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moment
        fields = ['time', 'goal', 'who_scored']

class PerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performance
        fields = ['home_points', 'home_goal_scored', 'home_goal_conceded', 'away_points', 'away_goal_scored', 'away_goal_conceded']

class TeamScoreStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamScoreStats
        fields = ['home_score_average', 'away_score_average', 'home_scoring_rate', 'away_scoring_rate']

class GameSerializer(serializers.ModelSerializer):
    performances = PerformanceSerializer(many=True)
    moments = MomentSerializer(many=True)
    team_score_stats = TeamScoreStatsSerializer()

    class Meta:
        model = Game
        fields = ['id_game', 'date', 'game', 'home', 'away', 'season', 'league', 'hour_game', 'performances', 'moments', 'team_score_stats']
