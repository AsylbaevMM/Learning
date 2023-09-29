from django.shortcuts import render
from hw2.models import Client, Product, Order
# Create your views here.


def clients_list(request):
    clients_list = Client.objects.all()

    # Постраничная разбивка с 3 постами на страницу
    paginator = Paginator(clients_list, 5)
    page_number = request.GET.get('page', 1)
    try:
        clients = paginator.page(page_number)
    except PageNotAnInteger:
        clients = paginator.page(1)
    except EmptyPage:
        clients = paginator.page(paginator.num_pages)
    return render(request,
                  'blog/post/list.html',
                  {'posts': posts,
                   'tag': tag})