from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView
from .models import KeyText, GenText, Blog, Partner, Product
from core.serializers import KeyTextSerializer, GenTextSerializer, ProductsSerializer, BlogsSerializer, PartnersSerializer, TariffsSerializer
from rest_framework import viewsets, permissions


class KeyTextCreateView(CreateAPIView):
    queryset = KeyText.objects.all()
    serializer_class = KeyTextSerializer
    

class GenTextRetrieveView(RetrieveAPIView):
    queryset = GenText.objects.all()
    serializer_class = GenTextSerializer    

class ProductsList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = [permissions.AllowAny]

class ProductsRetrieve(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = [permissions.AllowAny]

class BlogsList(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogsSerializer
    permission_classes = [permissions.AllowAny]

class BlogsRetrieve(RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogsSerializer
    permission_classes = [permissions.AllowAny]

class PartnersList(ListAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnersSerializer
    permission_classes = [permissions.AllowAny]

class PartnersRetrieve(RetrieveAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnersSerializer
    permission_classes = [permissions.AllowAny]

class TariffsList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = TariffsSerializer
    permission_classes = [permissions.AllowAny]

class TariffsRetrieve(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = TariffsSerializer
    permission_classes = [permissions.AllowAny]    

