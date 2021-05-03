from django.db import models

# Create your models here.

class test_1(models.Model):
    id = models.AutoField(primary_key=True)
    ip = models.CharField(max_length=50, verbose_name='ip Адрес')
    date = models.CharField(max_length=50, verbose_name='Дата и время запроса')
    method = models.CharField(max_length=1500, verbose_name='Метод запроса')
    url = models.CharField(max_length=1500, verbose_name='URL запроса')
    status_code = models.CharField(max_length=4, verbose_name='Код ответа')
    response_size = models.PositiveIntegerField(default=0, verbose_name='Размер ответа')

    def __str__(self):
        return self.ip

    class Meta:
        verbose_name = 'LogEntry'
        verbose_name_plural = 'LogEntry'

