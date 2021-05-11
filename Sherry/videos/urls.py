from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('get_videos/<int:last>/', views.get_videos, name='get_videos'),
    path('video/<int:id>', views.video, name='video'),
    path('playlist/<int:id>', views.playlist, name='playlist'),
    path('video/playlist_update', views.playlist_update, name='playlist_update'),
]