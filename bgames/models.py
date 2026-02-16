from django.db import models

class Bgame(models.Model):
    bgg_game_id = models.BigIntegerField(
        unique=True,
    )
    title = models.CharField(
        max_length=1024,
        )
    title_ru = models.CharField(
        max_length=1024,
        null=True,
        blank=True,
        default=None,
    )
    year = models.IntegerField(
        null=True,
        blank=True,
        default=None,
    )
    rank = models.IntegerField(
        null=True,
        blank=True,
        default=None,
    )
    voters_count = models.IntegerField(
        default=0,
    )
    bgg_rating = models.FloatField(
        default=0.0,
    )
    avg_rating = models.FloatField(
        default=0.0,
    )
