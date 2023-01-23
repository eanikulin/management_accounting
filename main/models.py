import datetime

from django.contrib.auth.models import User
from django.db import models

TYPE_CHOICES = (
    ("income", "приход"),
    ("outcome", "расход"),
)


class Document(models.Model):
    name = models.CharField(max_length=10, choices=TYPE_CHOICES, default="income")
    date = models.DateField(verbose_name='Дата в документе', blank=True, null=True, default=datetime.date.today)
    organization = models.ForeignKey('Organization', on_delete=models.PROTECT)
    invoice = models.ForeignKey('Invoice', on_delete=models.PROTECT)
    article = models.ForeignKey('Article', on_delete=models.PROTECT)
    analytics = models.ForeignKey('Analytics', on_delete=models.PROTECT)
    amount = models.FloatField(verbose_name='Сумма', blank=True, null=True)

    time_create = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True, blank=True, null=True)
    time_update = models.DateTimeField(verbose_name='Дата изменения', auto_now=True, blank=True, null=True)
    is_published = models.BooleanField(default=True)
    author = models.ForeignKey(User, verbose_name='Автор документа', on_delete=models.CASCADE, default=1)
    # Поменять на текущего юзера автоматом


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Документ"
        # verbose_name_prural = "Документ"
        ordering = ['-time_create', 'name']


class Organization(models.Model):
    name = models.CharField(verbose_name='Название организации', max_length=100, unique=True)
    description = models.CharField(blank=True, null=True, max_length=100)
    time_create = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    time_update = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name


class Invoice(models.Model):
    name = models.CharField(verbose_name='Название счета', max_length=100, unique=True)
    description = models.CharField(blank=True, null=True, max_length=100)
    time_create = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    time_update = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    name = models.CharField(verbose_name='Название статьи', max_length=100, unique=True)
    description = models.CharField(blank=True, null=True, max_length=100)
    time_create = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    time_update = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name


class Analytics(models.Model):
    name = models.CharField(verbose_name='Название аналитики', max_length=100, unique=True)
    description = models.CharField(blank=True, null=True, max_length=100)
    time_create = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    time_update = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name
