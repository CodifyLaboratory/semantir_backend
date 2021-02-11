from django.db import models
from django.contrib.auth.models import User

# Create your models 
class Products(models.Model):
    user = models.ForeignKey(
        to=User,
        related_name="order",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
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

class User(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    first_name=models.TextField(blank=False,null=True)
    emil = models.EmailField(blank=False, max_length=254, )
    date_joined=models.DateTimeField(auto_now_add=True)
    is_organizer=models.BooleanField(default=False)
    
class KeyText(models.Model):
    key_word = models.TextField(max_length=500, verbose_name="Текст для генерации")
    created_keytext_date = models.DateTimeField(auto_now_add=True, )
    


class GenText(models.Model):
    gen_text = "key_word" + "some gentext"
    created_gentext_date = models.DateTimeField(auto_now_add=True, )