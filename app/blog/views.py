import re

from django.http import HttpResponse
from django.shortcuts import render

from .models import Post


def post_list(request):
    posts = Post.objects.order_by('-created_date')
    context = {
        'posts': posts,
    }
    return render(request, 'blog/post_list.html', context)


def post_detail(request, pk):
    pk = Post.objects.get(id=pk)
    context = {
        'pk': pk,
    }
    return render(request, 'blog/post_detail.html', context)
