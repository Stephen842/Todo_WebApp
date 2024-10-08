from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Todo
from .forms import TodoForm
from datetime import datetime
from django.utils import timezone
import random
from django.db.models import Q
from django.views.generic import TemplateView, ListView
 
 #this modules below is for user authentication part and registration
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
 
# Create your views here.

def home(request):
    return render(request, 'todo/home.html')

@login_required
def todo(request):
    #Get the todos for the currently logged-in user only
    item = Todo.objects.filter(user=request.user).order_by('-date')

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user #Attach the logged in user
            todo.save()
            return redirect('todo')
    else:
        form = TodoForm()

    current_datetime = datetime.now()

    context = {
            'form': form,
            'item': item,
            'title': 'Todo List',
            'date': current_datetime,
            }
    return render(request, 'todo/todo.html', context)

#this function below is to have access by linking items so as to get access to what is stored in them. i call it details
@login_required
def details(request, id):
    item_details = get_object_or_404(Todo, id=id, user=request.user) #To user ownership
    list1 = Todo.objects.filter(user=request.user).order_by('-date') #Only shows user's todos
    context = {
            'item': item_details,
            'list1': list1
            }
    return render(request, 'todo/details.html', context)

# this function below update an item in the todo list
@login_required
def update(request, item_id):
    todo = get_object_or_404(Todo, id=item_id, user=request.user) #Ensures user ownership
    item = Todo.objects.filter(user=request.user).order_by('-date')

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo')
    else:
        form = TodoForm(instance=todo)

    context ={
            'form': form,
            'todo': todo,
            'item': item,
            }
    return render(request, 'todo/todo.html', context)

# this function below removes item from the todo list
@login_required
def remove(request, item_id):
    item = get_object_or_404(Todo, id=item_id, user=request.user) #Ensures user ownership
    item.delete()
    messages.info(request, 'item removed')
    return redirect('todo')

# this function below is to include the search bar to search through items that are store in the database
class SearchResultsViews(ListView):
    model = Todo
    template_name = 'todo/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('search_field')
        object_list = Todo.objects.filter(
                Q(title__icontains = query)
                )
        return object_list


def register(request):
    form = UserRegisterForm()

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()

            user.save()

            user_password = form.cleaned_data.get('password1')



            messages.success(request, 'Account created successfully ! You can now log in')

            user = authenticate(username = user.username, password = user_password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Error Processing Your Request')
        
    context = {'form': form, 'title': 'Register Here'}
    return render(request, 'todo/signup.html', context)

### login forms function below ###

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)

        if user is not None:
            form = auth_login(request, user)
            return redirect('home')
        else:
            messages.info(request, f'Invalid username or password. Please try again')
    form = AuthenticationForm() 
    return render(request, 'todo/login.html', {'form': form, 'title': 'Login'})

def sign_out(request):
    logout(request)
    return redirect('home')