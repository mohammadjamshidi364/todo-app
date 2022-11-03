from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required

from .models import TodoItem
from .forms import CreateTodoItem , UpdateTodoItem


def todoItems(request):
    
    user = request.user
    # get all todo items of user
    if request.user.is_authenticated:
        todo_items = TodoItem.objects.filter(user=user , completed=False)
    else:
        todo_items = {}
    
    context = {'todo_items':todo_items}
    return render(request , 'todo_app/todo_items.html' , context)

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