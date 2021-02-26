from rest_framework import serializers
from .models import KeyText, GenText, Products, Blogs, Partners

class KeyTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyText
        fields = ["word"]

class GenTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenText
        fields = ["gen_text"]

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