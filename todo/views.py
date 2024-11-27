from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Tag
from .forms import TagForm, TaskForm

def home(request):
    tasks = Task.objects.all().order_by('is_done', '-created_at')
    return render(request, 'todo/home.html', {'tasks': tasks})


def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            # Зберігаємо task
            task = form.save(commit=False)
            task.created_at = now()
            task.save()


            return redirect('todo:home')
    else:
        form = TaskForm()

    return render(request, 'todo/add_task.html', {'form': form})

def toggle_task_status(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_done = not task.is_done
    task.save()
    return redirect('todo:home')

def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        task.content = request.POST.get('content')
        task.deadline = request.POST.get('deadline') or None
        task.tags.clear()
        tags = request.POST.getlist('tags')
        for tag_id in tags:
            tag = Tag.objects.get(id=tag_id)
            task.tags.add(tag)

        task.save()
        return redirect('todo:home')

    tags = Tag.objects.all()
    return render(request, 'todo/update_task.html', {'task': task, 'tags': tags})


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('todo:home')


def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'todo/tags.html', {'tags': tags})


def add_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tags_list')
    else:
        form = TagForm()
    return render(request, 'todo/add_tag.html', {'form': form})

def update_tag(request, id):
    tag = get_object_or_404(Tag, id=id)
    if request.method == 'POST':
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            return redirect('tags_list')
    else:
        form = TagForm(instance=tag)
    return render(request, 'todo/update_tag.html', {'form': form})

def delete_tag(request, id):
    tag = get_object_or_404(Tag, id=id)
    tag.delete()
    return redirect('tags_list')