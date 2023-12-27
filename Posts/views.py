from django.shortcuts import render, redirect
from .models import Post
from django.urls import reverse
from .forms import AddPostForm


def show_list_posts(request):
    template ='Posts/posts_list.html'
    posts_list = Post.objects.all()
    context = {
        'posts_list': posts_list
    }
    return render(request, template, context)


def add_animal_breed(request):
    template = 'Posts/post_add.html'
    form = AddPostForm(request.POST, request.FILES)
    model = Post

    if request.method == 'POST':
        if form.is_valid():
            model.object = form.save()
            model.object.save()
            return redirect('/posts')
    context = {
        'form': form
    }
    return render(request, template, context)
