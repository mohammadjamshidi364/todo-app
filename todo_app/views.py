from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required

from .models import TodoItem , Workspace
from .forms import CreateTodoItem , UpdateTodoItem , CreateWorkspace


def todoItems(request):
    
    user = request.user
    # get all todo items of user
    if request.user.is_authenticated:
        todo_items = TodoItem.objects.filter(user=user , completed=False)
    else:
        todo_items = {}
    # get all completed todo items of user
    if request.user.is_authenticated:
        todo_completed = TodoItem.objects.filter(user=user , completed=True)
    else:
        todo_completed = {}
    
    # get workspaces 
    if request.user.is_authenticated:
        workspaces = Workspace.objects.filter(user=user)
    else:
        workspaces = {}
        
    context = {'todo_items':todo_items , 'todo_completed':todo_completed , 'workspaces':workspaces}
    return render(request , 'todo_app/todo_items.html' , context)

login_required('register')
def createWorkspace(request):
    form = CreateWorkspace()
    
    if request.method == 'POST':
        form = CreateWorkspace(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user = request.user
            user.save()
            return redirect('todo_items')

    context = {"form":form}
    return render(request , 'todo_app/create_workspace.html' , context)

login_required('register')
def createItem(request):
    form = CreateTodoItem()
    
    
    if request.method == 'POST':
        form = CreateTodoItem(request.POST)
        context = {'form':form}
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todo_items')
        
    context = {'form':form}
    
    return render(request , 'todo_app/create_todo.html', context)



def showTodoItem(request , pk):
    todo = TodoItem.objects.get(id=pk)
    form = UpdateTodoItem()
    
    if request.method == 'POST':
        
          
        form = UpdateTodoItem(request.POST , instance=todo, )
        if form.is_valid():
            form.save()
            return redirect('todo_items')
            
    context = {'todo':todo , 'form':form}
    return render(request , 'todo_app/show_todo_item.html' , context)

login_required('register')
def updateItem(request , pk):
    todo = TodoItem.objects.get(id=pk)
    form = UpdateTodoItem(instance=todo)
    
    if request.method == 'POST':
        form = UpdateTodoItem(request.POST , instance=todo)
        
        if form.is_valid():
            form.save()
            return redirect('todo_items')
    context = {'form':form}
    return render(request , 'todo_app/update_todo.html' , context)

login_required('register')
def deleteTodoItem(request , pk):
    todo = TodoItem.objects.get(id=pk)
    
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_items')
    
    return render(request , 'todo_app/delete_todo.html', context={'obj':todo})
