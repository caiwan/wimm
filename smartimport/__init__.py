# coding: utf-8
"""
This module contains the smart ai-enhanced import features
"""

from django.apps import AppConfig

default_app_config = 'smartimport.ItemConfig'

class ItemConfig(AppConfig):
    name = 'smartimport'

    def ready(self):
        import smartimport.api
