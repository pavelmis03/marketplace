from django.contrib import admin
from oscar.core.loading import get_model

Market = get_model('catalogue', 'Market')

admin.site.register(Market)

# Обязательный импорт остальных регистраций моделей
from oscar.apps.catalogue.admin import *  # noqa

Product