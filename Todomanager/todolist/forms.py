from django import forms
from todolist .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=['task', 'is_completed'] # __all__

#From todolist.html name=task is same as this forms.py task name.