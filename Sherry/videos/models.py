from django.db import models
from django.contrib.auth.models import User

from profiles.models import Profile

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}'


class Video(models.Model):

    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)

    tags = models.ManyToManyField(Tag, blank=True)

    title = models.CharField(max_length=100)
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
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f'{self.content}'


class Playlist(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    videos = models.ManyToManyField(Video, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    choice_access = [
        ('S', 'System'),
        ('U', 'User'),
    ]
    access = models.CharField(max_length=1, choices=choice_access, default='U')
    choice_privacy = [
        ('Pv','Private'),
        ('Pb','Public'),
        ('Fs','For Subscribers'),
    ]
    privacy = models.CharField(max_length=2, choices=choice_privacy, default='Pb')

    title = models.CharField(max_length=50, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.title} - {self.author}'