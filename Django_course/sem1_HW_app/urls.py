from django.urls import path
from .views import home, about

urlpatterns = [path("about/", about, name="about"),
    path("", home, name="home"),
               ]
