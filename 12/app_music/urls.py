from django.urls import path
from app_music import views


urlpatterns = [
    path('', views.home),
]
