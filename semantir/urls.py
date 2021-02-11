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
from rest_framework import routers 




router = routers.DefaultRouter()
# router.register(r'product', views.ProductsList, basename='Products')
# router.register(r'blog', views.BlogsList, basename='Blogs')
# router.register(r'partner', views.PartnersList, basename='Partners')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/all/', views.ProductsList.as_view()),
    path('blogs/all/', views.BlogsList.as_view()),
    path('partners/all/', views.PartnersList.as_view()),
    path('products/add/', views.ProductsCreate.as_view()),
    path('blogs/add/', views.BlogsCreate.as_view()),
    path('partners/add/', views.PartnersCreate.as_view()),
    path('products/<pk>/', views.ProductsDetail.as_view()),
    path('blogs/<pk>/', views.BlogsDetail.as_view()),
    path('partners/<pk>/', views.PartnersDetail.as_view()),
    path('products/<pk>/update/', views.ProductsUpdate.as_view()),
    path('blogs/<pk>/update/', views.BlogsUpdate.as_view()),
    path('partners/<pk>/update/', views.PartnersUpdate.as_view()),
    path('products/<pk>/destroy/', views.ProductsDestroy.as_view()),
    path('blogs/<pk>/destroy/', views.BlogsDestroy.as_view()),
    path('partners/<pk>/destroy/', views.PartnersDestroy.as_view()),
    path("auth/", include('djoser.urls')),
    path("auth/", include('djoser.urls.authtoken')),
    path("auth/", include('djoser.urls.jwt')),
    path("keytext/create/", views.KeyTextCreate.as_view()),
    
]

urlpatterns += router.urls