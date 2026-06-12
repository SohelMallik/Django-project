from django.shortcuts import render
from .models import Task #Import Task model from models.py

# Views connect with Templates
def homepage(request):
    context={
        'page' :'homepage'
    }
    return render(request, 'main.html', context)

def aboutus(request):
    context={
        'page' :'aboutus page'
    }
    return render(request, 'aboutus.html', context)

def contact(request):
    context={
        'page' :'contact page'
    }
    return render(request, 'contact.html', context)


def todolist(request):

    all_tasks= Task.objects.all() # get all the tasks from database as Objects

    context={
        'page' :'todolist page',
        'all_tasks': all_tasks,
    }
    return render(request, 'todolist.html', context)