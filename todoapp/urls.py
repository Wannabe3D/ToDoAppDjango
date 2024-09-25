from django.urls import path
from . import views

app_name = 'todoapp'

urlpatterns = [
    path('', views.index, name='index'),  # Основная страница
    path('task/<int:task_id>/edit', views.edit_task, name='edit_task'),
    path('task/<int:task_id>/', views.complete_task, name='complete_task'),
    path('task/add_task', views.add_task, name='add_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
]