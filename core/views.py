from rest_framework import viewsets
from rest_framework.generics import *
from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerProfileOrReadOnly


class ProductsList(ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer



class BlogsList(ListAPIView):
    queryset = Blogs.objects.all()
    serializer_class = BlogsSerializer



class PartnersList(ListAPIView):
    queryset = Partners.objects.all()
    serializer_class = PartnersSerializer

class UserProfileListCreateView(ListCreateAPIView):
    queryset=userProfile.objects.all()
    serializer_class=userProfileSerializer
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(user=user)


class UserProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset=userProfile.objects.all()
    serializer_class=userProfileSerializer
    permission_classes=[IsOwnerProfileOrReadOnly,IsAuthenticated]

class UserProfileList(ListAPIView):
    queryset=userProfile.objects.all()
    serializer_class=userProfileSerializer