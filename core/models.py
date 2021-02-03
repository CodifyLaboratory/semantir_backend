from django.db import models
from django.contrib.auth.models import User

# Create your models 
class Products(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название продукта")
    text = models.TextField(max_length=400, verbose_name="Текст")
    image = models.ImageField(verbose_name="Фотография продукта")
    
class Blogs(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок статьи")
    text = models.TextField(verbose_name="Текст статьи")
    publicated_date = models.DateTimeField(auto_now_add=True, null=True, )
    blogs_image = models.ImageField(verbose_name="Фотография для статьи")
    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
    
class Partners(models.Model):
    partners_image = models.ImageField(verbose_name="Фотография партнера")

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    first_name=models.TextField(blank=False,null=True)
    last_name=models.TextField(blank=False,null=True)
    emil = models.EmailField(blank=False, max_length=254, **options)
    description=models.TextField(blank=True,null=True)
    location=models.CharField(max_length=30,blank=True)
    date_joined=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
    is_organizer=models.BooleanField(default=False)
    image=models.ImageField(verbose_name="Фотография профиля")
    
    def __str__(self):
        return self.user.username