from django.core.management.base import BaseCommand
from hw2.models import Client


class Command(BaseCommand):
    help = 'create client, accepts "name email phone address"'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='clientname')
        parser.add_argument('email', type=str, help='client email')
        parser.add_argument('phone', type=str, help='client phone number' )
        parser.add_argument('address', type=str, help='clients_address_use_snakecase')

    def handle(self, *args, **kwargs):
        client = Client(name=kwargs['name'],
                        email=kwargs['email'],
                        phone=kwargs['phone'],
                        address=kwargs['address'])
        client.save()
        self.stdout.write(str(client))
