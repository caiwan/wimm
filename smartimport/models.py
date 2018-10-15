# coding: utf-8

from django.db import models
from django.utils.translation import ugettext_lazy as _

from item.models import TaggedItem

class RawItem(models.Model):
    content = models.TextField()
    type = models.IntegerField(null=False, default=0)
    item = models.OneToOneField(TaggedItem, default = None, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return '#{id} {created_at}: {content}: {item}'.format(
            id=self.id, created_at=self.created_at, content=self.content, item=str(self.item)
        )
