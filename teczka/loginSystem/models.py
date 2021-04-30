from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20)
    date = models.DateField(editable=True, blank=True, null=True)
    choices_gender = [
        ('M', 'Mężczyzna'),
        ('K', 'Kobieta'),
    ]
    gender = models.CharField(max_length=1, choices=choices_gender, default='M')
    phone_number = models.CharField(max_length=9, blank=True, null=True) #todo
    description = models.TextField(blank=True)
    picture = models.ImageField(default='default.jpg', upload_to='avatars')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.picture.path)

        if img.height > 256 or img.width > 256:
            output_size = (256, 256)
            img.thumbnail(output_size)
            img.save(self.picture.path)