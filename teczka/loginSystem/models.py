from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20, default='nickname')
    #data
    #plec
    #tel
    description = models.TextField(default='Jakis opis')
    picture = models.ImageField(default='default.jpg', upload_to='avatars')

    def __str__(self):
        return f'{self.user.username} Profile'
