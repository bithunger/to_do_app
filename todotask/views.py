from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from todotask.models import task
from django.contrib.auth import authenticate, login as authlogin, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required(login_url='login')
def home(request):
    context = {
        'usertask': task.objects.filter(user__id=request.user.id),
        'count': task.objects.filter(user__id=request.user.id, complete=False).count(),
    }
    search = request.GET.get('search')
    if search:
        context['usertask'] = context['usertask'].filter(
            title__icontains=search)
        context['search'] = search

    return render(request, 'todolist/home.html', context)


@login_required(login_url='login')
def create(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.user.username)
        title = request.POST['task-title']
        des = request.POST['task-des']

        usertask = task(user=user, title=title, des=des)
        usertask.save()

        messages.success(request, 'Task successfully created')
        return redirect('home')

    return render(request, 'todolist/createtask.html')


@login_required(login_url='login')
def update(request, slug):
    data = task.objects.get(user_slug=slug)
    if request.method == "POST":
        data.title = request.POST['task-title']
        data.des = request.POST['task-des']
        data.complete = False
        if request.POST.get('complete'):
            data.complete = request.POST.get('complete')
        data.save()

        messages.success(request, 'Task successfully updated')
        return redirect('home')

    return render(request, 'todolist/edit.html', {'task': data})


@login_required(login_url='login')
def delete(request, slug):
    data = task.objects.get(user_slug=slug)
    if request.method == 'POST':
        data.delete()
        messages.success(request, "Successfully delete")
        return redirect('home')
    return render(request, 'todolist/delete.html', {'task': data})
