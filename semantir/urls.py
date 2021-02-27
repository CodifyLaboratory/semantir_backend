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
from core import views
from core.models import User
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('key-text/create/', views.KeyTextCreateView.as_view(), name='create-key-text'),
    path('gen-text/retrieve/<int:pk>/', views.GenTextRetrieveView.as_view(), name='retrieve-gen-text'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
    path('products/all/', views.ProductsList.as_view()),
    path('blogs/all/', views.BlogsList.as_view()),
    path('partners/all/', views.PartnersList.as_view()),
    path('product/<pk>/', views.ProductsRetrieve.as_view()),
    path('blog/<pk>/', views.BlogsRetrieve.as_view()),
    path('partner/<pk>/', views.PartnersRetrieve.as_view()),

]

urlpatterns += router.urls