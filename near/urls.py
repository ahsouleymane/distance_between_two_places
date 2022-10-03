from django.urls import path
from near import views

urlpatterns = [
    path('', views.home, name="home"),
    path('coordonnees/', views.coordonnees, name="coordonnees"),
]