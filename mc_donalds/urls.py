from django.contrib import admin
from django.urls import path
from mc_donalds import views


urlpatterns = [
    path('', views.index),
]
