from django.db import models

class Task(models.Model):
    description = models.CharField(max_length=30, verbose_name='Краткое описание', null=False, blank=False)
    detail_description = models.TextField(verbose_name='Подробное описание', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')
    type = models.ManyToManyField('webapp.Type', verbose_name='Тип', related_name='type_tasks')
    status = models.ForeignKey('webapp.Status', verbose_name='Статус', related_name='status_tasks',
                               on_delete=models.RESTRICT, null=True, blank=True)
    project = models.ForeignKey('webapp.Project', verbose_name='Проект', related_name='project_tasks'
                                ,on_delete=models.RESTRICT, null=False, blank=False, )


    def __str__(self):
        return f"{self.id} | {self.description} "

    class Meta:
        db_table = 'tasks'
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'