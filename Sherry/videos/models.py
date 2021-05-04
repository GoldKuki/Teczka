from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tags(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}'


class Video(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    tags = models.ManyToManyField(Tags, blank=True)

    title = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    thumbnail = models.ImageField(default='user.jpg', upload_to='thumbnails')
    video = models.FileField(null=True, blank=True, upload_to='videos')
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    # doto profil
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f'{self.content}'