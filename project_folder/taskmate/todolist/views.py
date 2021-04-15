from django.shortcuts import render, redirect
from django.http import HttpResponse
from todolist.models import TaskList
from todolist.forms import TaskForm
from django.contrib import messages


# Create your views here.
def landing_page(request):

    if request.method == "POST":
        # connecting to the form
        # form checks if the field is empty or not and passes request.POST or None
        form = TaskForm(request.POST or None)
        # checking if the data we are provided with are valid
        if form.is_valid():
            form.save()

        messages.success(request, 'Task added successfully')

        return redirect('landing_page')

    else:
        all_tasks = TaskList.objects.all

        return render(request, 'todolist.html', {'all_tasks': all_tasks})


def edit_task(request, task_id):
    if request.method == 'POST':
        # we select a task to edit
        task = TaskList.objects.get(pk=task_id)
        # instance helps the database to recognise which task to edit
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid:
            form.save()

        messages.success(request, 'Task edited')

        return redirect('landing_page')

    else:
        task_obj = TaskList.objects.get(pk=task_id)

        return render(request, 'edit.html', {'task_obj': task_obj})


def contact(request):

    context = {
        'contact_text': 'Welcome to the Contact Page',
    }

    return render(request, 'contact.html', context)


def about(request):

    context = {
        'about_text': 'Welcome to the About Page',
    }

    return render(request, 'about.html', context)


def delete_task(request, task_id):

    task = TaskList.objects.get(pk=task_id)
    task.delete()

    return redirect('landing_page')


def change_status(request, task_id):

    task = TaskList.objects.get(pk=task_id)

    if task.done == False:
        task.done = True
        task.save()
    else:
        task.done = False
        task.save()

    return redirect('landing_page')
