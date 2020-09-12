import random
from django.core.management.base import BaseCommand
from blog.models import Gallery
from django_seed import Seed

class Command(BaseCommand):

    help = "This command creates Gallery Photo"

    def add_arguments(self, parser):
        parser.add_argument("--number", help="How many users do you want to create")

    def handle(self, *args, **options):
        seeder = Seed.seeder()
        number = options.get("number")
        seeder.add_entity(
            Gallery,
            31,
            {
                "thumb": lambda x: f"room_photos/{random.randint(1, 31)}.webp",
                "photo_small": None,
                "photo_large": None,
                "description": lambda x: seeder.faker.text(),
            },
        )
        seeder.execute()

        self.stdout.write(self.style.SUCCESS("Gallery created!"))