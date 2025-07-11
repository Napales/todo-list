from django.db import models

status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]

class Type(models.Model):
    name = models.CharField(max_length=30, verbose_name='Тип', null=False, blank=False, unique=True)

    def __str__(self):
        return f"{self.id} | {self.name} "

    class Meta:
        db_table = 'Type'
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'


class Status(models.Model):
    name = models.CharField(max_length=30, verbose_name='Статус', null=False, blank=False, unique=True)

    def __str__(self):
        return f"{self.id} | {self.name} "

    class Meta:
        db_table = 'Status'
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Task(models.Model):
    description = models.CharField(max_length=30, verbose_name='Краткое описание', null=False, blank=False)
    detail_description = models.TextField(verbose_name='Подробное описание', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')
    type = models.ForeignKey('webapp.Type', verbose_name='Тип', on_delete=models.RESTRICT, null=True, blank=True)
    status = models.ForeignKey('webapp.Status', verbose_name='Статус', on_delete=models.RESTRICT, null=True, blank=True)


    def __str__(self):
        return f"{self.id} | {self.description} "

    class Meta:
        db_table = 'tasks'
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'



