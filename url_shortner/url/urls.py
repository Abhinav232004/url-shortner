from django.contrib import admin
from django.urls import path,include
from .views import shorten,index

urlpatterns = [
    path('short/',index , name="index"),
    path("<str:id>/",shorten,name="shorten"),
]