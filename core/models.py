from django.db import models

class KeyText(models.Model):
    key_word = models.TextField(max_length=250, verbose_name="Текст для генерации")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания" )
    def __str__(self):
        return self.key_word
    