from django.db import models
from django.contrib.auth.models import User


class Clients(models.Model):
    name = models.CharField(max_length=100, blank=False, verbose_name='Имя клиента')
    surname = models.CharField(max_length=100, blank=False, verbose_name='Фамилия клиента')
    address = models.CharField(max_length=100, blank=True, verbose_name='Адрес клиента')
    telephone = models.CharField(max_length=100, blank=False, verbose_name='Телефон клиента')
    birth_day = models.DateField(max_length=100)
    hobbies = models.ManyToManyField('Hobbies', blank=True, verbose_name='Хобби')
    categories = models.ManyToManyField('Categories', blank=True, verbose_name='Категория фильмов')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name='Дата обновления')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='media/clients/%Y/%m/%d', verbose_name='Изображение', blank=True)

    class Meta:
        verbose_name = 'Клиенты'
        verbose_name_plural = 'Клиент'
        ordering = ['-created_at']

    def __str__(self):
        return self.name + ' ' + self.surname


class Hobbies(models.Model):
    title = models.CharField(max_length=100, blank=False)

    class Meta:
        verbose_name = 'Хобби'
        verbose_name_plural = 'Хобби'

    def __str__(self):
        return self.title


class Categories(models.Model):
    title = models.CharField(max_length=100, blank=False)

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категория'

    def __str__(self):
        return self.title


