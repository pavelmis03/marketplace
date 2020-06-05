from django.db.models.query import QuerySet
from oscar.apps.dashboard.catalogue.views import *


class ProductListView(ProductListView):
    def get_queryset(self):
        """
        Build the queryset for this list
        """
        all_products = list(Product.objects.browsable_dashboard())
        products = []
        for product in all_products:
            if product.market.owner is self.request.user:
                products.append(product)
        queryset = QuerySet(model=Product, using=products)
        queryset = self.filter_queryset(queryset)
        queryset = self.apply_search(queryset)
        return queryset
