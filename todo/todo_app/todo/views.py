from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Todo
from .forms import TodoForm
from datetime import datetime
from django.utils import timezone
import random

# Create your views here.

def home(request):
    return render(request, 'todo/home.html')

def todo(request):
    item = Todo.objects.order_by('-date')
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    form = TodoForm()

    current_datetime = datetime.now()


    page = {
            'forms': form,
            'list': item,
            'title': 'Todo List',
            'date': current_datetime,
            }
    return render(request, 'todo/todo.html', page)

# this function below update an item in the todo list
def update(request, item_id):
    todo = Todo.objects.get(id = item_id)
    form = TodoForm(instance = todo)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance = todo)
        if form.is_valid():
            form.save()
            return redirect('todo')
    else:
        form = TodoForm(instance=todo)

    context ={
            'form': form,
            'todo': todo,
            }
    return render(request, 'todo/todo.html', context)

# this function below removes item from the todo list
def remove(request, item_id):
    item = Todo.objects.get(id = item_id)
    item.delete()
    messages.info(request, 'item removed')
    return redirect('todo')
