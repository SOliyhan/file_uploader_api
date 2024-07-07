from django.db import models


class Game(models.Model):
    app_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    release_date = models.DateField()
    required_age = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    dlc_count = models.IntegerField()
    about_the_game = models.TextField()
    supported_languages = models.TextField()

    on_windows = models.BooleanField()
    on_mac = models.BooleanField()
    on_linux = models.BooleanField()

    positive = models.IntegerField()
    negative = models.IntegerField()
    score_rank = models.FloatField(blank=True, null=True)

    developers = models.CharField(max_length=255)
    publishers = models.CharField(max_length=255, null=True)

    categories = models.CharField(max_length=255, null=True)
    genres = models.CharField(max_length=255, null=True)
    tags = models.CharField(max_length=255, null=True)
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
    
