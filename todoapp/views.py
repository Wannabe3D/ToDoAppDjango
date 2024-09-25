from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.http import Http404
from django.contrib.auth import logout



# Create your views here.
def index(request):
    if request.user.is_authenticated:
        tasks = Task.objects.filter(owner=request.user)
    else:
        tasks = None
    context = {'tasks': tasks}
    return render(request, 'todoapp/index.html', context)
@login_required
def add_task(request):
    """Позволяет добавить новую задачу"""
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.owner = request.user
            new_task.save()
            return redirect('todoapp:index')
    else:
        form = TaskForm()

    context = {'form': form}
    return render(request, 'todoapp/add_task.html', context)
@login_required
def edit_task(request, task_id):
    """Редактирует задачу"""
    task = get_object_or_404(Task, id=task_id)

    # Проверка того, что тема принадлежит текущему пользователю.
    if task.owner != request.user:
        raise Http404
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)  # Создаем форму, используя существующий экземпляр задачи

        if form.is_valid():  # Проверяем валидность данных
            form.save()  # Сохраняем данные, если форма валидна
            return redirect('todoapp:index')  # Перенаправляем пользователя после успешного сохранения

    else:
        form = TaskForm(instance=task)  # Если это GET-запрос, используем существующие данные задачи в форме

    context = {'form': form, 'task': task}
    return render(request, 'todoapp/task_edit.html', context)
@login_required
def complete_task(request, task_id):
    """Помечает задачу, как завершённую"""
    task = get_object_or_404(Task, id=task_id)
    if task.owner != request.user:
        raise Http404
    if request.method == 'POST':
        task.completed = not task.completed
        task.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if task.owner != request.user:
        raise Http404
    if request.method == 'POST':
        task.delete()
    return redirect('todoapp:index')

