from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from .forms import ImageForm
from hw2.models import Product


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            print(image)
            product_id = form.cleaned_data['id']
            product = Product.objects.filter(id=product_id).first()
            fs = FileSystemStorage()
            print(f'{image.name=}')
            print(f"{image=}")
            fs.save(image.name, image)
            product.image=image
            product.save()

    else:
        form = ImageForm
    return render(request, 'hw4/upload_image.html', {'form': form})




