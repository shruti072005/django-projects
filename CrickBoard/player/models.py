from django.db import models

# Create your models here.
class player(models.Model):
    jn = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    runs = models.IntegerField()
    wickets = models.IntegerField()
    teamname = models.CharField(max_length=100)

    def __str__(self):
        return self.name