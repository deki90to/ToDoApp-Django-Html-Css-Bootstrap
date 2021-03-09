from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import *
from . forms import *

def index(request):
	todo = ToDo.objects.all()
	form = ToDoForm()

	if request.method == 'POST':
		form = ToDoForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('index')

	context = {'todo':todo, 'form':form}
	return render(request, 'todo_app/list.html', context)

def update(request, pk):
	todo = ToDo.objects.get(id=pk)
	form = ToDoForm(instance=todo)

	if request.method == 'POST':
		form = ToDoForm(request.POST, instance=todo)
		if form.is_valid():
			form.save()
			return redirect('index')

	context = {'todo':todo, 'form':form}
	return render(request, 'todo_app/update.html', context)

def delete(request, pk):
	task = ToDo.objects.get(id=pk)

	if request.method == 'POST':
		task.delete()
		return redirect('index')

	context = {'task':task}
	return render(request, 'todo_app/delete.html', context)