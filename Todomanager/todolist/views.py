from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'main.html', {})

def aboutus(request):
    return render(request, 'aboutus.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def todolist(request):
    return render(request, 'todolist.html', {})