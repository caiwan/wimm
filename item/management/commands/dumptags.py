import json

from django.core.management.base import BaseCommand, CommandError
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase
from taggit.models import Tag

from item.models import TaggedItem

class Command(BaseCommand):
    """
    """

    def add_arguments(self, parser):
        # parser.add_argument('poll_id', nargs='+', type=int)
        pass

    def handle(self, *args, **options):
        tag_list = []
        for tag in Tag.objects.all():
            tag_list.append({
                'name' : tag.name,
                'slug' : tag.slug,
                'count': tag.taggit_taggeditem_items.count()
            })

        print(json.dumps(tag_list))

        pass

    pass
