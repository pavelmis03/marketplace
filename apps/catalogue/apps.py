"""Модуль с конфигурацией приложения 'catalogue'"""
import oscar.apps.catalogue.apps as apps


class CatalogueConfig(apps.CatalogueConfig):
    """Конфигурация прирожения 'catalogue'"""
    label = 'catalogue'
    name = 'apps.catalogue'
    verbose_name = 'Каталог'
