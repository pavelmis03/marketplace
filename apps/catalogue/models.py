from django.contrib.auth.models import User  # noqa isort:skip
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from oscar.apps.catalogue.abstract_models import AbstractProduct
from oscar.models.fields.slugfield import SlugField


class Market(models.Model):
    """
    Модель подмагазина.

    `name` — название

    `slug` — уникальное имя

    `description` — описание
    
    `owner` — пользователь-владелец
    """
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, default=1)
    name = models.CharField(_('Name'), max_length=255, db_index=True)
    slug = SlugField(_('Slug'), max_length=255, db_index=True, unique=True)
    description = models.TextField(_('Description'), blank=True)
    image = models.ImageField(_('Image'), upload_to='markets', blank=True,
                              null=True, max_length=255)

    class Meta:
        app_label = 'catalogue'
        ordering = ['name']
        verbose_name = "Магазин"
        verbose_name_plural = "Магазины"

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('market-detail', args=(self.slug, ))


class MarketManager(models.Model):
    """
    Модель для создания менеджеров подмагазинов.
    Соединяет модель магазина и модель пользователя.
    """
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    market = models.ForeignKey(to=Market, on_delete=models.CASCADE)


class Product(AbstractProduct):
    """
    Переопределённая модель товара для того, чтобы
    товар мог принадлежать подмагазину.
    """
    market = models.ForeignKey(to=Market, on_delete=models.CASCADE,
                               null=True, blank=True)


# ОБЯЗАТЕЛЬНЫЙ ИМПОРТ ОСТАЛЬНЫХ МОДЕЛЕЙ
from oscar.apps.catalogue.models import *

Category  # Чтобы PyCharm не предлагал убрать этот импорт как неиспользуемый
