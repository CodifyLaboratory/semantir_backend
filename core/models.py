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
        return self.key_word


class GenText(models.Model):
    gen_text = models.TextField(verbose_name="Сгенерированный текст")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")        
    
class User(models.Model):
    user = models.ForeignKey(KeyText, on_delete=models.CASCADE, related_name="profile")
    email = models.EmailField(blank=False, max_length=254, )
    date_joined=models.DateTimeField(auto_now_add=True)
    is_organizer=models.BooleanField(default=False)