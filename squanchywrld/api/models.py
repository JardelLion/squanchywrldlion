import uuid
from django.db import models

# Create your models here.

class Game(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # UUID como chave primária
    date = models.DateField()
    home_team = models.CharField(max_length=100)
    away_team = models.CharField(max_length=100)
    result = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.date} - {self.home_team} vs {self.away_team}"
    

class Goal(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # UUID como chave primária
    game = models.ForeignKey(Game, related_name='goals', on_delete=models.CASCADE)
    time = models.CharField(max_length=10)
    goal = models.CharField(max_length=10)
    who_scored = models.CharField(max_length=100)  # Corrigido o nome da variável

    def __str__(self):
        return f"{self.who_scored} scored at {self.time} in {self.game}"




class Performance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='performance')
    home_points = models.IntegerField()
    home_scored = models.IntegerField()
    home_conceded = models.IntegerField()
    away_points = models.IntegerField()
    away_scored = models.IntegerField()
    away_conceded = models.IntegerField()

    def __str__(self):
        return f"Performance for {self.game}"