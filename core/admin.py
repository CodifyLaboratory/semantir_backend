from django.contrib import admin
from .models import *

class ProductsAdmin(admin.ModelAdmin):
    fields = ["name", "text", "image"]

class NewsAdmin(admin.ModelAdmin):
        fields = ["title", "text", "publicated_date", "news_image"]

class PartnersAdmin(admin.ModelAdmin):
        fields = ["partners_image"]

class UserProfileAdmin(admin.ModelAdmin):
        fields =["first_name", "last_name", "email", "image", "id"]
admin.site.register(Products)
admin.site.register(Blogs)
admin.site.register(Partners)
admin.site.register(UserProfile)
# Register your models here.
