from django.urls import path

from . import views

urlpatterns = [
    path('', views.homeDash, name='home-dash'),
]