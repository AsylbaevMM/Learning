from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "print 'Helloworld!' to output"

    def handle(self, *args, **options):
        self.stdout.write('Hello world!')