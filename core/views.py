from rest_framework import viewsets, permissions
from rest_framework.generics import ListAPIView, CreateAPIView,\
    UpdateAPIView, DestroyAPIView
from .serializers import *
from .models import *

class ProductsList(ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = [permissions.AllowAny]

class ProductsCreate(CreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        print("Product created!")
        return super().post(request, *args, **kwargs)

class ProductsDetail(ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProductsUpdate(UpdateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProductsDestroy(DestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = [permissions.IsAuthenticated]

class BlogsList(ListAPIView):
    queryset = Blogs.objects.all()
    serializer_class = BlogsSerializer
    permission_classes = [permissions.AllowAny]

class BlogsCreate(CreateAPIView):
    queryset = Blogs.objects.all()
    serializer_class = BlogsSerializer
    permission_classes = [permissions.IsAuthenticated]

class BlogsDetail(ListAPIView):
    queryset = Blogs.objects.all()
    serializer_class = BlogsSerializer
    permission_classes = [permissions.IsAuthenticated]

class BlogsUpdate(UpdateAPIView):
    queryset = Blogs.objects.all()
    serializer_class = BlogsSerializer
    permission_classes = [permissions.IsAuthenticated]

class BlogsDestroy(DestroyAPIView):
    queryset = Blogs.objects.all()
    serializer_class = BlogsSerializer
    permission_classes = [permissions.IsAuthenticated]



class PartnersList(ListAPIView):
    queryset = Partners.objects.all()
    serializer_class = PartnersSerializer
    permission_classes = [permissions.AllowAny]

class PartnersCreate(CreateAPIView):
    queryset = Partners.objects.all()
    serializer_class = PartnersSerializer
    permission_classes = [permissions.IsAuthenticated]

class PartnersDetail(ListAPIView):
    queryset = Partners.objects.all()
    serializer_class = PartnersSerializer
    permission_classes = [permissions.IsAuthenticated]

class PartnersUpdate(UpdateAPIView):
    queryset = Partners.objects.all()
    serializer_class = PartnersSerializer
    permission_classes = [permissions.IsAuthenticated]

class PartnersDestroy(DestroyAPIView):
    queryset = Partners.objects.all()
    serializer_class = PartnersSerializer
    permission_classes = [permissions.IsAuthenticated]

class KeyTextCreate(CreateAPIView):
    queryset = KeyText.objects.all()
    serializer_class = KeyTextSerializer
    permission_classes = [permissions.AllowAny]

