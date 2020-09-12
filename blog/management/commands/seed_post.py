import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from blog.models import Post, Category, Like, Gallery
from django.contrib.admin.utils import flatten

class Command(BaseCommand):

    help = "This command creates posts"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many rooms you want to create"
        )

    def handle(self, *args, **options):
        tags = [
            "Aniaml ",
            "Coffee",
            "Cake",
            "Room",
            "World",
            "Peace",
            "Elephant",
            "Cats",
            "Dogs",
        ]

        number = options.get("number")
        seeder = Seed.seeder()
        all_like = Like.objects.all()
        all_category = Category.objects.all()
        all_photos = Gallery.objects.all()
        seeder.add_entity(
            Post,
            number,
            {
                "title": lambda x: seeder.faker.name(),
                "body": lambda x: seeder.faker.text(),
                "intro": lambda x: seeder.faker.text(),
                "category": lambda x: random.choice(all_category),
                "read_time": lambda x: random.randint(1, 30),
                "photo": lambda x: random.choice(all_photos),
                "tags": lambda x: random.choice(tags),
                "slug": None
            },
        )

        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"{number} rooms created!"))
