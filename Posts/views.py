from django.shortcuts import render
from .models import Post


def show_list_posts(request):
    template ='Posts/posts_list.html'
    posts_list = Post.objects.all()
    context = {
        'posts_list': posts_list
    }
    return render(request, template, context)