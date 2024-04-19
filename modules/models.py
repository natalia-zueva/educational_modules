from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Module(models.Model):
    title = models.CharField(max_length=500, verbose_name='название')
    description = models.TextField(**NULLABLE, verbose_name='описание')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Модуль'
        verbose_name_plural = 'Модули'
