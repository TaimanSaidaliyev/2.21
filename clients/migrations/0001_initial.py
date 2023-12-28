# Generated by Django 4.2.8 on 2023-12-28 05:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Категории',
                'verbose_name_plural': 'Категория',
            },
        ),
        migrations.CreateModel(
            name='Hobbies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Хобби',
                'verbose_name_plural': 'Хобби',
            },
        ),
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя клиента')),
                ('surname', models.CharField(max_length=100, verbose_name='Фамилия клиента')),
                ('address', models.CharField(blank=True, max_length=100, verbose_name='Адрес клиента')),
                ('telephone', models.CharField(max_length=100, verbose_name='Телефон клиента')),
                ('birth_day', models.DateField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('photo', models.ImageField(blank=True, upload_to='media/clients/%Y/%m/%d', verbose_name='Изображение')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('categories', models.ManyToManyField(blank=True, to='clients.categories', verbose_name='Хобби')),
                ('hobbies', models.ManyToManyField(blank=True, to='clients.hobbies', verbose_name='Хобби')),
            ],
            options={
                'verbose_name': 'Клиенты',
                'verbose_name_plural': 'Клиент',
                'ordering': ['-created_at'],
            },
        ),
    ]