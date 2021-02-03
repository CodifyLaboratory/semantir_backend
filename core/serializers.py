from rest_framework import serializers
from .models import *

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ["id","name", "text", "image"]

class BlogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogs
        fields = ["id","title", "text", "publicated_date", "blogs_image"]

class PartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partners
        fields = ["id","partners_image"]

class userProfileSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=userProfile
        fields='__all__'