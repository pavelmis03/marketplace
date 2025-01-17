"""Views for 'API' app"""
# pylint: disable=too-many-ancestors,missing-class-docstring
from django.contrib.auth.models import Group, User
from django.contrib.sites.models import Site
from rest_framework import permissions
from rest_framework import generics, viewsets
from oscar.apps.basket.models import Basket, Line as BasketLine
from oscar.apps.catalogue.models import ProductClass, Category
from oscar.apps.order.models import Order, Line as OrderLine, ShippingAddress, \
    OrderNote
from oscar.apps.partner.models import Partner, StockRecord


from apps.catalogue.models import Product, Market
from api.serializers import UserSerializer, GroupSerializer, \
    ProductSerializer, ProductClassSerializer, OrderSerializer, \
    OrderNoteSerializer, CategorySerializer, SiteSerializer, BasketSerializer, \
    ShippingAddressSerializer, BasketLineSerializer, OrderLineSerializer, \
    StockRecordSerializer, PartnerSerializer, MarketSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class MarketViewSet(viewsets.ModelViewSet):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer
    permission_classes = [permissions.IsAuthenticated]


#
# class ProductList(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#
# class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


class ProductClassViewSet(viewsets.ModelViewSet):
    queryset = ProductClass.objects.all()
    serializer_class = ProductClassSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrderLineViewSet(viewsets.ModelViewSet):
    queryset = OrderLine.objects.all()
    serializer_class = OrderLineSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrderNoteViewSet(viewsets.ModelViewSet):
    queryset = OrderNote.objects.all()
    serializer_class = OrderNoteSerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class SiteViewSet(viewsets.ModelViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
    permission_classes = [permissions.IsAuthenticated]


class BasketViewSet(viewsets.ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    permission_classes = [permissions.IsAuthenticated]


class BasketLineViewSet(viewsets.ModelViewSet):
    queryset = BasketLine.objects.all()
    serializer_class = BasketLineSerializer
    permission_classes = [permissions.IsAuthenticated]


class ShippingAddressViewSet(viewsets.ModelViewSet):
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializer
    permission_classes = [permissions.IsAuthenticated]


class StockRecordViewSet(viewsets.ModelViewSet):
    queryset = StockRecord.objects.all()
    serializer_class = StockRecordSerializer
    permission_classes = [permissions.IsAuthenticated]


class PartnerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    permission_classes = [permissions.IsAuthenticated]
