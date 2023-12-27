from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя продукта')
    description = models.TextField(verbose_name='Описание продукта')
    category = models.ForeignKey('ProductCategory', on_delete=models.CASCADE, verbose_name='Категория')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(verbose_name='Количество')
    date_added = models.DateField(auto_now_add=True, verbose_name='Дата добавления')
    photo = models.ImageField(upload_to='media/breeds/%Y/%m/%d', verbose_name='Изображение', blank=True)

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    category_name = models.CharField(max_length=100)
    category_description = models.TextField()

    def __str__(self):
        return self.category_name