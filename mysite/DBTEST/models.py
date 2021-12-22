from django.db import models

class Articles(models.Model):
    title = models.CharField('Назва',max_length=50,default='Something')
    anons = models.CharField('Анонс', max_length=250, default='Something')
    full_text = models.TextField('Стаття')
    date = models.DateTimeField('Дата Публікації')

    def __str__(self):
        return f'Новина: {self.title}'

    class Meta:
        verbose_name = 'Новина'
        verbose_name_plural = 'Новини'

    def get_absolute_url(self):
        return f'/news/{self.id}'



