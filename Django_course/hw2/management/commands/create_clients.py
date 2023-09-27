from django.core.management.base import BaseCommand
from hw2.models import Client


class Command(BaseCommand):
    help = 'create clients, accepts count of clients'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='count')


    def handle(self, *args, **kwargs):
        clients_count = Client.objects.count()
        for i in range(clients_count, clients_count+kwargs['count']):
            client = Client(name=f'Client{i}',
                            email=f'Client{i}@mail.com',
                            phone=f'{i}'.rjust(10, '0'),
                            address=f'Client {i} address')
            client.save()
            self.stdout.write(str(client))
        self.stdout.write(f'{kwargs["count"]} clients created')