from django.shortcuts import render, redirect
from .models import Task, Article, Comment
from .forms import TaskForm, TaskToDelete
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
import json


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})

def articles(request):
    articles = Article.objects.order_by('-pub_date')[:5]
    return render(request, 'main/articles.html', {'title': 'Главная страница сайта', 'articles': articles})

def detail(request, article_id):
    try:
        a = Article.objects.get(id = article_id)
    except:
        raise Http404("Статья не найдена!")
    
    latest_comment_list = a.comment_set.order_by('-id')[:10]
    return render(request, 'main/detail.html', {'article': a, 'latest_comment_list': latest_comment_list})

def leave_comment(request, article_id):
    try:
        a = Article.objects.get(id = article_id)
    except:
        raise Http404("Статья не найдена!")
    
    a.comment_set.create(author_name = request.POST['name'], comment_text = request.POST['text'])
    return HttpResponseRedirect( reverse('detail', args = (a.id,)) )

def about(request):
    return render(request, 'main/about.html')


def create(request):
    error=''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма некорректна'

    form = TaskForm()
    context = {'form' : form, 'error': error}
    return render(request, 'main/create.html', context)


def delete(request):
    error=''
    if request.method == 'POST':
        requestid = request.POST.get("idel")
        TaskWeDelete = Task.objects.filter(id=requestid)
        TaskWeDelete.delete()
    tasks = Task.objects.order_by('-id')
    form = TaskToDelete()
    context = {'form' : form, 'error': error, 'tasks': tasks}
    return render(request, 'main/delete.html', context)