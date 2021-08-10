from django.db import models
from django.db.models.deletion import CASCADE
from .game_rating import GameRating

class Game(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    designer = models.CharField(max_length=100)
    number_of_players = models.IntegerField()
    est_time = models.CharField(max_length=20)
    age_rec = models.CharField(max_length=100)
    category = models.ForeignKey("Category", on_delete=CASCADE)

    @property
    def average_rating(self):
        """Average rating calculated attribute for each game"""
        ratings = GameRating.objects.filter(game=self)

        # Sum all of the ratings for the game
        total_rating = 0
        for rating in ratings:
            total_rating += rating.rating
        
        if total_rating == 0:
            return 0
        else:
            avg_rating = round((total_rating / len(ratings)), 2)
            return avg_rating