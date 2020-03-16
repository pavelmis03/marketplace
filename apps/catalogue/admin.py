from django.contrib import admin
from oscar.core.loading import get_model
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
#
Market = get_model('catalogue', 'Market')
# from apps.catalogue.models import Market
#
#

# class MarketAdmin():
#     form = movenodeform_factory(Market)
#     list_display = ('name', 'slug')


admin.site.register(Market)
#
from oscar.apps.catalogue.admin import *  # noqa
