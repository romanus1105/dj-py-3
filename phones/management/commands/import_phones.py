import csv
from pprint import pprint

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    help = """Add phones from CSV-file to DB. 
    Format of CSV should be like - 
    id;name;image;price;release_date;lte_exists"""

    def add_arguments(self, parser):
        parser.add_argument('file', type = str, help = 'path to CSV-file')

    def handle(self, *args, **options):
        with open(options['file'], 'r') as f:
            phones = list(csv.DictReader(f, delimiter=';'))
        for phone in phones:
            # TODO: Добавьте сохранение модели
            _phone = Phone(
                name = phone['name'], 
                price = phone['price'],
                image = phone['image'],
                release_date = phone['release_date'],
                lte_exists = phone['lte_exists'],
                slug = phone['name'].lower().replace(' ', '')
            )
            _phone.save()

