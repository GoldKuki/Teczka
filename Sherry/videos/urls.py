from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('video/<int:id>', views.video, name='video'),
    path('playlist/<int:id>', views.playlist, name='playlist'),
]