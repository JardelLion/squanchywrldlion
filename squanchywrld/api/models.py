from django.db import models

class Game(models.Model):
    id = models.UUIDField(primary_key=True)
    id_game = models.CharField(max_length=100)
    date = models.CharField(max_length=50, null=True, blank=True)
    game = models.CharField(max_length=100)
    home = models.CharField(max_length=50)
    away = models.CharField(max_length=50)
    season = models.CharField(max_length=20)
    league = models.CharField(max_length=50)
    hour_game = models.CharField(max_length=10)

    def __str__(self):
        return self.game


class Performance(models.Model):
    game = models.ForeignKey(Game, related_name="performances", on_delete=models.CASCADE)
    home_points = models.IntegerField(null=True, blank=True)
    home_goal_scored = models.IntegerField(null=True, blank=True)
    home_goal_conceded = models.IntegerField(null=True, blank=True)
    away_points = models.IntegerField(null=True, blank=True)
    away_goal_scored = models.IntegerField(null=True, blank=True)
    away_goal_conceded = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Performance for {self.game}"


class Moment(models.Model):
    game = models.ForeignKey(Game, related_name="moments", on_delete=models.CASCADE)
    time = models.CharField(max_length=10)
    goal = models.CharField(max_length=10)
    who_scored = models.CharField(max_length=100)

    def __str__(self):
        return f"Moment in {self.game}: {self.time} - {self.who_scored}"


class TeamScoreStats(models.Model):
    game = models.ForeignKey(Game, related_name="team_score_stats", on_delete=models.CASCADE)
    home_score_average = models.FloatField(null=True, blank=True)
    away_score_average = models.FloatField(null=True, blank=True)
    home_scoring_rate = models.CharField(max_length=10)
    away_scoring_rate = models.CharField(max_length=10)

    def __str__(self):
        return f"Score stats for {self.game}"
