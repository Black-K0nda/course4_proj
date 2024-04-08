from django.core.management.base import BaseCommand

from movies.omdb_integration import search_and_save
# import django
# import os

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'site.settings')
# django.setup()

class Command(BaseCommand):
    help = "Search OMDb and populates the database with results"

    def add_arguments(self, parser):
        parser.add_argument("search", nargs="+")

    def handle(self, *args, **options):
        search = " ".join(options["search"])
        search_and_save(search)