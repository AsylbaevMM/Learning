from django.core.management.base import BaseCommand
from hw2.models import Client, Product, Order
from random import choice, sample, randint

class Command(BaseCommand):
    help = 'create orders, accepts count of orders'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='count')


    def handle(self, *args, **kwargs):
        clients_count = Client.objects.count()
        products_count = Product.objects.count()
        for _ in range(kwargs['count']):
            items = Product.objects.order_by('?')[:randint(1, products_count//10)]
            order = Order(client=choice(Client.objects.all()),
                            total_price = sum(i.price for i in items))
            order.save()
            for item in items:
                order.products.add(item)
            order.save()
            self.stdout.write(str(order))
        self.stdout.write(f'{kwargs["count"]} orders created')