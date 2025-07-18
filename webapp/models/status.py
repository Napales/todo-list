from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=30, verbose_name='Статус', null=False, blank=False, unique=True)

    def __str__(self):
        return f"{self.id} | {self.name} "

    class Meta:
        db_table = 'Status'
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'