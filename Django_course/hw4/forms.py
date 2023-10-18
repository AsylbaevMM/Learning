from django import forms
from hw2.models import Product

class ImageForm(forms.Form):
    id = forms.IntegerField(max_value=Product.objects.all().count()-1)
    image = forms.ImageField()
