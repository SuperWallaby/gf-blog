from django.core.management.base import BaseCommand
from blog.models import Site
from django_seed import Seed

class Command(BaseCommand):

    help = "This command creates many users"

    def add_arguments(self, parser):
        parser.add_argument("--number", help="How many users do you want to create")

    def handle(self, *args, **options):
        Site.objects.create(title="Crisma my love",key_words="bear, love",description_short="crisma's lovely blog",email="colton950901@gmail.com")
        self.stdout.write(self.style.SUCCESS("Categories created!"))