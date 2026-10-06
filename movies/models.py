from django.db import models

# Create your models here.

class Movie(models.Model):
    name=models.CharField(max_length=200)
    language=models.CharField(max_length=500)
    duration=models.IntegerField(max_length=20)
    director=models.CharField(max_length=200)
    release_date=models.DateField()