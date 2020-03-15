import oscar.apps.dashboard.reviews.apps as apps


class ReviewsDashboardConfig(apps.ReviewsDashboardConfig):
    label = 'reviews_dashboard'
    name = 'apps.dashboard.reviews'
    verbose_name = 'Панель отзывов'
