from django.http import HttpResponseRedirect
from django.shortcuts import render

from webapp.models import Task, status_choices


def index(request):
    tasks = Task.objects.order_by('-compelet_date')
    return render(request, 'index.html', {"tasks": tasks})


def create_task(request):
    if request.method == "POST":
        description = request.POST.get("description")
        status = request.POST.get("status")
        compelet_date = request.POST.get("complet_date")
        Task.objects.create(description=description, status=status, compelet_date=compelet_date)
        return HttpResponseRedirect("/")
    else:
        return render(request, 'create_task.html', {'status_choices': status_choices})
