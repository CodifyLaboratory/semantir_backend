from rest_framework import viewsets, permissions
from rest_framework.generics import ListAPIView, CreateAPIView,\
    UpdateAPIView, DestroyAPIView, RetrieveAPIView
from .serializers import *
from .models import *

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

class KeyTextCreate(CreateAPIView):
    queryset = KeyText.objects.all()
    serializer_class = KeyTextSerializer
    permission_classes = [permissions.IsAuthenticated]

