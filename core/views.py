from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from .models import KeyText, GenText
from core.serializers import KeyTextSerializer, GenTextSerializer


class KeyTextCreateView(CreateAPIView):
    queryset = KeyText.objects.all()
    serializer_class = KeyTextSerializer
    

class GenTextRetrieveView(RetrieveAPIView):
    queryset = GenText.objects.all()
    serializer_class = GenTextSerializer    

