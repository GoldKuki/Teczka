from django.db import models
from django.contrib.auth.models import User

from PIL import Image


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    nickname = models.CharField(max_length=20)
    image = models.ImageField(default='user.jpg', upload_to='profil_pics')
    backgraund = models.CharField(max_length=6, null=True)
    choice_gender = [
        ('M', 'Mężczyzna'),
        ('K', 'Kobieta'),
        ('N', 'Nieokreślone'),
    ]
    gender = models.CharField(max_length=1, choices=choice_gender, default='N')
    choice_gender = [
        ('PL', 'Polska'),
        ('ENG', 'England'),
        ('N', 'Nieokreślone'),
    ]
    country = models.CharField(max_length=3, choices=choice_gender, default='N')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.nickname}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.width > 256 or img.height > 256:
            output_size = (256, 256)
            img.thumbnail(output_size)
            img.save(self.image.path)
