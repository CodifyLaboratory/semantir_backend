from rest_framework import serializers
from .models import KeyText

class KeyTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyText
        fields = ["word"]