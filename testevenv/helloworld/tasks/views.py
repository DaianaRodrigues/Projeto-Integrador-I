from django.shortcuts import render
from django.http import HttpResponse


def helloworld(request):
    return HttpResponse('Hello World!')

def taskList(request):
    return render(request, 'tasks/list.html')


