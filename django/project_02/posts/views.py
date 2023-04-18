from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):

    posts = Post.objects.all()
    context = {
        'posts':posts,
    }

    return render(request, 'posts/index.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:index')
    else:
        form = PostForm()
    context = {
        'form':form,
    }
    return render(request, 'posts/create.html', context)


def detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        'post':post,
    }
    return render(request, 'posts/detail.html', context)


@login_required
def delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('posts:index')


@login_required
def update(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:detail', post.pk)
    else:
        form = PostForm(instance=post)
    context = {
        'form':form,
        'post':post,
    }
    return render(request, 'posts/update.html', context)


def category(request, subject):
    post = Post.objects.filter(category=subject)
    print(post)
    context = {
        'post': post,
    }
    return render(request, 'posts/category.html', context)


def info(request):

    return render(request, 'posts/info.html')
