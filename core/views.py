from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .models import KeyText
from core.serializers import KeyTextSerializer


class KeyTextCreateView(CreateAPIView):
    queryset = KeyText.objects.all()
    serializer_class = KeyTextSerializer
    
# Create your views here.
