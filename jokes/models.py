from django.db import models


class Joke(models.Model):
    content = models.TextField(verbose_name='Текст')
    published = models.DateTimeField(auto_now_add=True, db_index=True)
    likes = models.IntegerField(default='0', editable=False)
    rubric = models.ManyToManyField('Rubric', blank=False, )

    class Meta:
        verbose_name = 'Анекдот'
        verbose_name_plural = 'Анекдоты'
        ordering = ['-published']


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Рубрика'
        verbose_name_plural = 'Рубрики'
        ordering = ['name']


