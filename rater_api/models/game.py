from django.db import models
from django.db.models.deletion import CASCADE

class Game(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    designer = models.CharField(max_length=100)
    number_of_players = models.IntegerField()
    est_time = models.CharField(max_length=20)
    age_rec = models.CharField(max_length=100)
    player = models.ForeignKey("Player", on_delete=CASCADE)