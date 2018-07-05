import json

from django.db import transaction
from django.core.management.base import BaseCommand, CommandError
from taggit.managers import TaggableManager
from taggit.models import Tag

from item.models import TaggedItem

class Command(BaseCommand):
    """
    """

    def add_arguments(self, parser):
        # parser.add_argument('poll_id', nargs='+', type=int)
        pass

    def handle(self, *args, **options):
        with transaction.atomic():
            tags = Tag.objects.all()
            orphan_count = 0
            for tag in tags: 
                if tag.taggit_taggeditem_items.count() >0:
                    continue
                orphan_count = orphan_count + 1
                tag.delete()
              
            print('Removed {0} orphaned tags'.format(orphan_count))

        pass

    pass
