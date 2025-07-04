
from django.shortcuts import render, redirect, get_object_or_404

from webapp.forms import TaskForm
from webapp.models import Task, status_choices


def index(request):
    tasks = Task.objects.order_by('-compelet_date')
    return render(request, 'index.html', {"tasks": tasks})


def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect('index')
        else:
            return render(request, 'create_task.html', {'status_choices': status_choices, 'form': form})
    else:
        form = TaskForm()
        return render(request, 'create_task.html', {'status_choices': status_choices, 'form': form})


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        task.delete()
        return redirect('index')
    else:
        return render(request, 'task_delete.html', {'task': task})


def detail_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_detail.html', {'task': task})

def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect('index')
        else:
            return render(request, 'update_task.html', {"form": form})
    else:
        form = TaskForm(instance=task)
        return render (request, 'update_task.html', {"form": form, "task": task })

