from django.core.management.base import BaseCommand
from blog.models import Category
from django_seed import Seed

class Command(BaseCommand):

    help = "This command creates many users"

    def add_arguments(self, parser):
        parser.add_argument("--number", help="How many users do you want to create")

    def handle(self, *args, **options):
        seeder = Seed.seeder()

        amenities = [
            "Teaching ",
            "English",
            "Korean",
            "Cook",
            "Gaza",
            "Love",
            "Bears",
        ]
        
        for a in amenities:
            Category.objects.create(name=a,description=seeder.faker.text(),slug=None)
        self.stdout.write(self.style.SUCCESS("Categories created!"))