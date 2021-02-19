from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from .models import KeyText, GenText
from core.serializers import KeyTextSerializer, GenTextSerializers


class KeyTextCreateView(CreateAPIView):
    queryset = KeyText.objects.all()
    serializer_class = KeyTextSerializer
    

class GenTextRetrieveView(RetrieveAPIView):
    queryset = KeyText.objects.all()
    serializer_class = KeyTextSerializer    

