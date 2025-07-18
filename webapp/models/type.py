from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=30, verbose_name='Тип', null=False, blank=False, unique=True)

    def __str__(self):
        return f"{self.id} | {self.name} "

    class Meta:
        db_table = 'Type'
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'