from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from webapp.models import Task, status_choices


def index(request):
    tasks = Task.objects.order_by('-complete_date')
    return render(request, 'index.html', {"tasks": tasks})


def create_task(request):
    if request.method == "POST":
        description = request.POST.get("description")
        status = request.POST.get("status")
        complete_date = request.POST.get("complete_date")
        detail_description = request.POST.get("detail_description")
        Task.objects.create(description=description, status=status, complete_date=complete_date,
                            detail_description=detail_description)
        return redirect('index')
    else:
        return render(request, 'create_task.html', {'status_choices': status_choices})


def detail_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_detail.html', {'task': task})
