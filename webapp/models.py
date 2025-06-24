from django.db import models

status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]

class Task(models.Model):
    description = models.TextField(verbose_name='Описание', null=False, blank=False)
    status = models.CharField(max_length=20, verbose_name='Статус', choices=status_choices, default='new')
    compelet_date = models.DateField(verbose_name='Дата выполнения', null=True, blank=True)


    def __str__(self):
        return f"{self.id} | {self.description} "

    class Meta:
        db_table = 'tasks'


