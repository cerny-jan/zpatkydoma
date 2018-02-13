import os

from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.management import call_command

from wagtail.wagtailcore.models import Site, Page

# command to generate the data
# python manage.py dumpdata --natural-foreign --indent 2 -e auth.permission -e contenttypes -e wagtailcore.GroupCollectionPermission -e wagtailimages.rendition  -e sessions -e postgres_search.indexentry > tests/fixtures/test_data.json

class Command(BaseCommand):
    def handle(self, **options):
        fixtures_dir = os.path.join(settings.BASE_DIR, 'tests', 'fixtures')
        fixture_file = os.path.join(fixtures_dir, 'test_data.json')

        # Wagtail creates default Site and Page instances during install, but we already have
        # them in the data load. Remove the auto-generated ones.

        if Site.objects.filter(hostname='localhost').exists():
            Site.objects.get(hostname='localhost').delete()
        if Page.objects.filter(title='Welcome to your new Wagtail site!').exists():
            Page.objects.get(title='Welcome to your new Wagtail site!').delete()

        call_command('loaddata', fixture_file, verbosity=0)

        self.stdout.write(self.style.SUCCESS('Test data loaded!'))
