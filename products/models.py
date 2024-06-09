from django.db import models
from django.utils import timezone
from users.models import User


# Constants
NULLABLE = {'blank': True, 'null': True}

# Product
class Product(models.Model):
    '''Product model'''

    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор продукта', **NULLABLE)

    title = models.CharField(max_length=200, verbose_name='Название продукта')
    model = models.CharField(max_length=200, verbose_name='Модель продукта')
    release_date = models.DateTimeField(default=timezone.now, verbose_name='Дата выхода продукта на рынок')

    def __str__(self):
        return f'{self.title} - {self.model}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
