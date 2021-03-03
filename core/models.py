from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    use_in_migrations = True
    

    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(email, password, **extra_fields)
  
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()



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


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название продукта")
    text = models.TextField(max_length=400, verbose_name="Текст")
    image = models.ImageField(verbose_name="Фотография продукта")

class Blog(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок статьи")
    text = models.TextField(verbose_name="Текст статьи")
    publicated_date = models.DateTimeField(auto_now_add=True, null=True, )
    blogs_image = models.ImageField(verbose_name="Фотография для статьи")
    
    
class Partner(models.Model):
    partners_image = models.ImageField(verbose_name="Фотография партнера")

class Tariff(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название тарифа")
    text = models.TextField(verbose_name="Описание")
    price = models.PositiveIntegerField(verbose_name="Стоимость")
    image = models.ImageField(verbose_name="Фотография тарифа")    