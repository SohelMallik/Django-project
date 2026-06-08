from django.shortcuts import render

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
    context={
        'page' :'todolist page'
    }
    return render(request, 'todolist.html', context)