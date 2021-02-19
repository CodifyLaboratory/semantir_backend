from rest_framework import serializers
from .models import KeyText, GenText

class KeyTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyText
        fields = ["word"]

class GenTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenText
        fields = ["gen_text"]        