from django.db import models
from django.contrib.auth.models import User

class KeyText(models.Model):
    word = models.CharField(max_length=250, verbose_name="Ключевое слово")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    gen_text = models.OneToOneField(
        to="GenText",
        verbose_name="Сгенерированный текст",
        on_delete=models.SET_NULL,
        null=True,
        blank=True

    )

    def __str__(self):
        return self.word


class GenText(models.Model):
    gen_text = models.TextField(verbose_name="Сгенерированный текст")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")        
    
class User(models.Model):
    user = models.ForeignKey(KeyText, on_delete=models.CASCADE, related_name="profile")
    email = models.EmailField(blank=False, max_length=254, )
    date_joined=models.DateTimeField(auto_now_add=True)
    is_organizer=models.BooleanField(default=False)


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