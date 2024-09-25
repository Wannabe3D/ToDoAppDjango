from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'text', 'deadline', 'completed']
        labels = {
            'title': 'Задача',
            'text': 'Описание',
            'deadline': 'Срок',
            'completed': 'Выполнено',
        }
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date', 'required': False}),
            'title': forms.TextInput(attrs={'required': False, 'placeholder': 'Введите название задачи'}),
            'text': forms.Textarea(attrs={'required': False, 'placeholder': 'Введите описание задачи'}),
            'completed': forms.CheckboxInput(attrs={'required': False}),
        }
