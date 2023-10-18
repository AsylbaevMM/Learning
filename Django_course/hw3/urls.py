from django.urls import path
from .views import *


app_name = 'hw3'



urlpatterns = [
    path("", clients, name="clients"),
    path("client/<int:id>", client, name='client'),
    path("client/<int:id>/<str:times>", client, name='client'),
    path("order/<int:id>", order, name='order'),
    path("product/<int:id>", product, name='product'),
    ]