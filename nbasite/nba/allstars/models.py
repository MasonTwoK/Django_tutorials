from django.db import models
from datetime import datetime

# Create your models here.
class Position(models.Model):
    pos_name = models.CharField(max_length=16)
    pub_date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.pos_name

    def was_published_today(self):
        return self.pub_date.date() == datetime.now().date()


class Player(models.Model):
    player_name = models.CharField(max_length=144)
    votes = models.IntegerField(default=0)
    
    position = models.ForeignKey(to=Position, on_delete=models.CASCADE)

    def __str__(self):
        return self.player_name