from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from webapp.models import Task, status_choices


def index(request):
    tasks = Task.objects.order_by('-compelet_date')
    return render(request, 'index.html', {"tasks": tasks})


def create_task(request):
    if request.method == "POST":
        description = request.POST.get("description")
        status = request.POST.get("status")
        compelet_date = request.POST.get("compelet_date")
        detail_description = request.POST.get("detail_description")
        Task.objects.create(description=description, status=status, compelet_date=compelet_date,
                            detail_description=detail_description)
        return redirect('index')
    else:
        return render(request, 'create_task.html', {'status_choices': status_choices})
