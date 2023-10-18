from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    return HttpResponse("Hello, it's 2nd homework, use 'management' folder.")
