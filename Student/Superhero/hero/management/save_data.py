from json import dump
from django.core.management.base import BaseCommand
from hero.models import Superhero

class command(BaseCommand):

    def handle(self, *args, **options):
        save_data()

def save_data():
    for hero in Superhero.objects.all().values():
        print(hero)