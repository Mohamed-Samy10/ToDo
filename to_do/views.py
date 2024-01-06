from django.shortcuts import render , redirect
from .models import Task
from .forms import TaskForm
# Create your views here.
def do(request):
    tasks = Task.objects.all()
    form = TaskForm()
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid :
            form.save()
        return redirect('/')
    context ={'tasks':tasks,'form':form}
    return render (request,'to_do/task.html',context)

def updateTask(request,pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    
    if request.method == 'POST':
        form = TaskForm(request.POST,instance=task)
        if form.is_valid :
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request,'to_do/update_task.html',context)

def deleteTask(request,pk):
    task = Task.objects.get(id = pk)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    
    context = {'task':task}
    return render(request,'to_do/delete_task.html',context)
    
def addTask(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid :
            form.save()
        return redirect('/')
    context ={'form':form}
    return render (request,'to_do/add_task.html',context)
def taskDetails(request,pk):
    task = Task.objects.get(id = pk)
    form = TaskForm()
    context = {'task':task,'form':form}
    return render(request,'to_do/task_details.html',context)    



