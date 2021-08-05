from django.db import models
from django.db.models.deletion import CASCADE

class GameImage(models.Model):
    image = models.ImageField()
    player = models.ForeignKey("Player", on_delete=CASCADE)
    game = models.ForeignKey("Game", on_delete=CASCADE)