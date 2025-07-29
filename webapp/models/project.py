from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Project(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название', null=False, blank=False)
    description = models.TextField(verbose_name='Описание', null=False, blank=False)
    start_date = models.DateField(verbose_name='Дата начала', null=False, blank=False)
    end_date = models.DateField(verbose_name='Дата окончания', null=True, blank=True)
    user = models.ForeignKey(get_user_model(), verbose_name='Пользователь', related_name='user_projects',
                               on_delete=models.RESTRICT)

    def __str__(self):
        return f"{self.id} | {self.name} "

    class Meta:
        db_table = 'projects'
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def get_absolute_url(self):
        return reverse('webapp:project_detail', kwargs={'pk': self.pk})