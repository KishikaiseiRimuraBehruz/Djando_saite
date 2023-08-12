from django.db import models
# Create your models here.
class Creators(models.Model):
    title = models.CharField('Название', max_length=50)
    creator = models.CharField('Имя', max_length=250)
    full_text = models.TextField('Подробнее')
    date = models.DateTimeField('Дата')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Создатель'
        verbose_name_plural = 'Создатели'

class New(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Подробнее')
    date = models.DateTimeField('Дата')
    image = models.CharField(max_length=2083)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/creators/{self.id}'

    class News:
        verbose_name = 'Новый'
        verbose_name_plural = 'Новые'
