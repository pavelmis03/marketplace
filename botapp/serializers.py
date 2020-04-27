from django.contrib.auth.models import User, Group
from oscar.apps.catalogue.models import Product, ProductClass
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
        model = Product
        fields = ['parent', 'title', 'slug', 'description', 'product_class', 'categories', ]


class ProductClassSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductClass
        fields = ['name', 'slug', 'requires_shipping', 'track_stock']


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ['number', 'site', 'basket', 'user', 'billing_address', 'currency', 'shipping_address', 'shipping_method', 'shipping_code', 'status', 'guest_email']


class OrderNoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderNote
        fields = ['order', 'user', 'note_type', 'message', '']
