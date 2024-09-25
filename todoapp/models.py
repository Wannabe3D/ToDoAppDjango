from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    """Пользовательская задача на выполнение"""
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True, null=True)
    deadline = models.DateTimeField()
    completed = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'задача'
        verbose_name_plural = 'Задачи'
    def __str__(self):
        """Возвращает строковое представление модели"""
        if len(self.title) > 50:
            return f'{self.title}...'
        else:
            return self.title

