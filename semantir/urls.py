"""semantir URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core.views import *
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', ProductsList.as_view()),
    path('blogs/', BlogsList.as_view()),
    path('partners/', PartnersList.as_view()),
    path('users/', UserProfileList.as_view()),
    path('users/create/', UserProfileListCreateView.as_view()),
    path('users/update-destroy-retrieve/', UserProfileDetailView.as_view())

]
