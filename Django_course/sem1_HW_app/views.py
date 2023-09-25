import logging
from django.shortcuts import render


logger = logging.getLogger(__name__)

def home(request):
    logger.info('Homepage accessed')
    return render(request, "sem1_HW/home.html")



def about(request):
    logger.info('About page accessed')
    return render(request, "sem1_HW/about.html")

# Create your views here.
