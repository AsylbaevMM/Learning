from django.core.management.base import BaseCommand
from hw2.models import Product
from random import randint, uniform


class Command(BaseCommand):
    help = 'create products, accepts count of products'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='count')

    def handle(self, *args, **kwargs):
        clients_count = Product.objects.count()
        for i in range(clients_count, clients_count+kwargs['count']):
            product = Product(name=f'Product{i}',
                            description=f'Product {i} description',
                            price= uniform(1, 100000),
                            count=randint(1, 1000))
            product.save()
            self.stdout.write(str(product))
        self.stdout.write(f'{kwargs["count"]} clients created')