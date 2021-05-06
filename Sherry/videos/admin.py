from django.contrib import admin
from .models import Video, Comment, Tag, Playlist

# Register your models here.

admin.site.register(Video)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Playlist)