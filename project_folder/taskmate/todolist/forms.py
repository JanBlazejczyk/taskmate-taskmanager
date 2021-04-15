from django import forms
from todolist.models import TaskList


# which class you are connecting to?
class TaskForm(forms.ModelForm):  # import model form from forms
    class Meta:
        model = TaskList  # we have a model / database TaskList inside models.py
        fields = ['task', 'done']  # fields of the model / database
