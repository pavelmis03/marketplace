from django.contrib.auth.models import User, Group
from django.contrib.sites.models import Site
from oscar.apps.basket.models import Basket
from oscar.apps.catalogue.models import Product, ProductClass, Category
from oscar.apps.order.models import Order, OrderNote
from rest_framework import serializers


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
        model = Product  # TODO: change Model, add Markets
        fields = ['parent', 'title', 'slug', 'description',
                  'product_class', 'categories', ]


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
