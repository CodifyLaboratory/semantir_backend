from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView
from .models import KeyText, GenText, Blogs, Partners, Products
from core.serializers import KeyTextSerializer, GenTextSerializer, ProductsSerializer, BlogsSerializer, PartnersSerializer
from rest_framework import viewsets, permissions


class KeyTextCreateView(CreateAPIView):
    queryset = KeyText.objects.all()
    serializer_class = KeyTextSerializer
    

class GenTextRetrieveView(RetrieveAPIView):
    queryset = GenText.objects.all()
    serializer_class = GenTextSerializer    

class ProductsList(ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = [permissions.AllowAny]

class ProductsRetrieve(RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = [permissions.AllowAny]

class BlogsList(ListAPIView):
    queryset = Blogs.objects.all()
    serializer_class = BlogsSerializer
    permission_classes = [permissions.AllowAny]

class BlogsRetrieve(RetrieveAPIView):
    queryset = Blogs.objects.all()
    serializer_class = BlogsSerializer
    permission_classes = [permissions.AllowAny]

class PartnersList(ListAPIView):
    queryset = Partners.objects.all()
    serializer_class = PartnersSerializer
    permission_classes = [permissions.AllowAny]

class PartnersRetrieve(RetrieveAPIView):
    queryset = Partners.objects.all()
    serializer_class = PartnersSerializer
    permission_classes = [permissions.AllowAny]

