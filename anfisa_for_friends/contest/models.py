from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Contest(models.Model):
    title = models.CharField(max_length=20, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(
        verbose_name='Цена',
        validators=[MinValueValidator(10), MaxValueValidator(100)],
        help_text='Рекомендованная розничная цена'
    )
    comment = models.TextField(
        blank=True,
        verbose_name='Комментарий'
    )
    image = models.ImageField(
        'Изображение', upload_to='images', blank=True
    )

    def __str__(self):
        return self.title
