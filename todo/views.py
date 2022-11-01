from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo
from .forms import TodoForm


def homeTodo(request):
    todoLists = Todo.objects.all()
    title = 'Home Todo'
    context = {'todoLists': todoLists, 'title': title}

    return render(request, 'todo/home.html', context)

def detailTodo(request, todoId):

    todoDetails = get_object_or_404(Todo, id=todoId)
    title = 'Detail Todo'
    context = {'todoDetails': todoDetails, 'title': title}

    return render(request, 'todo/detail.html', context)

def createTodo(request):

    form = TodoForm()
    title = 'Create Todo'
    context = {'form': form, 'title': title}

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid:
            form.save()    

    return render(request, 'todo/create.html', context)

def updateTodo(request, todoId):

    todo = get_object_or_404(Todo, id=todoId)
    form = TodoForm(instance=todo)
    title = 'Update Todo'
    context = {'form': form, 'title': title}

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('detail-todo', todoId)

    return render(request, 'todo/update.html', context)

def deleteTodo(request, todoId):

    todo = get_object_or_404(Todo, id=todoId)
    title = 'Delete Todo'
    context = {'obj': todo, 'title': title}

    if request.method == 'POST':
        todo.delete()
        return redirect('home-todo')

    return render(request, 'todo/delete.html', context)
