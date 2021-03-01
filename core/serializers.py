from rest_framework import serializers
from .models import KeyText, GenText, Product, Blog, Partner

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
        model = Product
        fields = ["id","name", "text", "image"]

class BlogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ["id","title", "text", "publicated_date", "blogs_image"]


class PartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ["id","partners_image"]                