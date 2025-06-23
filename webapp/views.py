from django.http import HttpResponseRedirect
from django.shortcuts import render

from webapp.models import Task

def index(request):
    tasks = Task.objects.order_by('-compeletdate')
    return render(request, 'index.html', {"tasks": tasks})


def create_task(request):
    if request.method == "POST":
        desctiption = request.POST.get("description")
        status = request.POST.get("status")
        compelet_date = request.POST.get("completdate")
        Task.objects.create(desctiption=desctiption, status=status, compeletdate=compelet_date)
        return HttpResponseRedirect("/")
    else:
        return render(request, 'create_article.html')
