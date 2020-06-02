# pylint: disable=missing-class-docstring
from django.contrib.auth.models import User, Group
from django.contrib.sites.models import Site
from oscar.apps.basket.models import Basket, Line as BasketLine
from oscar.apps.catalogue.models import ProductClass, Category
from oscar.apps.order.models import Order, Line as OrderLine, OrderNote, \
    ShippingAddress
from oscar.apps.partner.models import StockRecord, Partner
from rest_framework import serializers

from apps.catalogue.models import Product, Market


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['market', 'parent', 'title', 'slug', 'description',
                  'product_class', 'categories', ]


class MarketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Market
        fields = ['owner', 'name', 'slug', 'description', 'image']


class ProductClassSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductClass
        fields = ['name', 'slug', 'requires_shipping', 'track_stock']


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ['number', 'site', 'basket', 'user', 'billing_address',
                  'currency', 'shipping_address', 'shipping_method',
                  'shipping_code', 'status', 'guest_email']


class OrderLineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderLine
        fields = [
            # PARTNER INFORMATION
            'order', 'partner', 'partner_name', 'partner_sku',
            'partner_line_reference', 'partner_line_notes', 'stockrecord',

            # PRODUCT INFORMATION
            'product', 'title', 'upc', 'quantity',

            # REPORTING INFORMATION
            'line_price_incl_tax', 'line_price_excl_tax',
            'line_price_before_discounts_incl_tax',
            'line_price_before_discounts_excl_tax',
            'unit_cost_price', 'unit_price_incl_tax',
            'unit_price_excl_tax', 'unit_retail_price',

            #
            'status', 'est_dispatch_date',
        ]


class OrderNoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderNote
        fields = ['order', 'user', 'note_type', 'message', ]


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'description', 'image', 'slug', ]


class SiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Site
        fields = ['domain', 'name', ]


class BasketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Basket
        fields = ['owner', 'status', 'vouchers', 'date_created',
                  'date_merged', 'date_submitted']


class BasketLineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BasketLine
        fields = ['basket', 'line_reference', 'product', 'stockrecord',
                  'quantity', 'price_currency', 'price_excl_tax',
                  'price_incl_tax', 'date_created']


class ShippingAddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = ['phone_number', 'notes', ]


class StockRecordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StockRecord
        fields = ['product', 'partner', 'partner_sku', 'price_currency',
                  'price_excl_tax', 'price_retail', 'cost_price',
                  'num_in_stock', 'num_allocated', 'low_stock_threshold',
                  'date_created', 'date_updated', ]


class PartnerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Partner
        fields = ['code', 'name', 'users', ]
