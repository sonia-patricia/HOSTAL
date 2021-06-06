from django.urls import path
from website import views

urlpatterns = [
    path('home', views.home)
]