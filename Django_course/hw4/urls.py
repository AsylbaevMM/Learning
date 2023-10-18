from django.urls import path
from .views import *


app_name = 'hw3'



urlpatterns = [
    path("upload/", upload_image, name="upload_image"),

    ]