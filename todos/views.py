from django.shortcuts import render, redirect

from .models import Todo
from .forms import TodoForm


def index(request):
    todos = Todo.objects.order_by('-id')
    todoForm = TodoForm()

    context = {
        'todos': todos,
        'todoForm': todoForm,
    }
    return render(request, 'todos/index.html', context)


def addtodo(request):
    print("In Post")
    print(request.POST)

    todoForm = TodoForm(request.POST)

    if todoForm.is_valid():
        todo = Todo(text=request.POST['text'])
        todo.save()
    else:
        print("Incorrect")

    return redirect('index')


def complete(request, todo_id):
    try:
        todo = Todo.objects.get(pk=todo_id)
        todo.complete = True
        todo.save()
    except:
        print("Todo Not Found.")

    return redirect('index')

def undocomplete(request, todo_id):
    try:
        todo = Todo.objects.get(pk=todo_id)
        todo.complete = False
        todo.save()
    except:
        print("Todo Not Found.")

    return redirect('index')


def delete(request, todo_id):
    try:
        todo = Todo.objects.get(pk=todo_id)
        todo.delete()
    except:
        print("Todo Not Found.")

    return redirect('index')
