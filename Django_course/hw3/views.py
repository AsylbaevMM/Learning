from django.shortcuts import render
from hw2.models import Client, Product, Order
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime, timedelta
from django.utils import timezone


def clients(request):
    clients = Client.objects.all()

    # Постраничная разбивка с 3 постами на страницу
    paginator = Paginator(clients, 10)
    page_number = request.GET.get('page', 1)
    try:
        clients = paginator.page(page_number)
    except PageNotAnInteger:
        clients = paginator.page(1)
    except EmptyPage:
        clients = paginator.page(paginator.num_pages)
    return render(request,
                  'hw3/clients.html',
                  {'clients': clients})

def client(request, id, times = None):
    client = Client.objects.filter(id=id).first()
    times = times or 'year'
    now = timezone.now()

    filter_times = {
        'week':  now - timedelta(days=7),
        'month': now - timedelta(days=30),
        'year': now - timedelta(days = 365)
    }

    if client:
        orders = Order.objects.filter(client = client, created__gte=filter_times[times])

        paginator = Paginator(orders, 10)
        page_number = request.GET.get('page', 1)
        try:
            orders = paginator.page(page_number)
        except PageNotAnInteger:
            orders = paginator.page(1)
        except EmptyPage:
            orders = paginator.page(paginator.num_pages)
        return render(request,
                      'hw3/orders.html',
                      {'client': client, 'orders':orders})
    else:
        return Http404


def order(request, id):
    order = Order.objects.filter(id=id).first()

    if order:
        products = order.products.all()
        return render(request,
                      'hw3/order.html',
                      {'order': order, 'products': products})
    else:
        return Http404


def product(request, id):
    product = Product.objects.filter(id=id).first()

    if order:

        return render(request,
                      'hw3/product.html',
                      {'product': product})
    else:
        return Http404