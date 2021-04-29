from django.db import models
from loginSystem.models import Profile

# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    thumbnail = models.ImageField()
    video = models.FileField()
    views = models.IntegerField(default=0)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    date = models.DateField()

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title