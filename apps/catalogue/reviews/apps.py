import oscar.apps.catalogue.reviews.apps as apps


class CatalogueReviewsConfig(apps.CatalogueReviewsConfig):
    label = 'reviews'
    name = 'apps.catalogue.catalogue.reviews'
    verbose_name = 'Отзывы каталога'
