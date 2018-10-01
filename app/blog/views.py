import re

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Post


def post_list(request):
    posts = Post.objects.order_by('-created_date')
    context = {
        'posts': posts,
    }
    return render(request, 'blog/post_list.html', context)


def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    context = {
        'post': post,
    }
    return render(request, 'blog/post_detail.html', context)


def post_create(request):
    """
    Template:   blog/post_create.html
    URL:        /posts/create/
    URL Name:   post-create

    템플릿에 하나의 <form>요소를 구현
        input[name="title"]
        textarea[name="text"]
        button[type="submit"]


    post_create.html을 보여주는 링크를 base.html에 구현
        {% url %}태그를 사용할
    :param request:
    :return:
    """
    if request.method == 'POST':
        # POST요청이 왔을 경우
        #   새 글을 작성하고 원하는 페이지로 돌아가도록 함
        # HttpResponse 를 돌려줌
        #   제목: <제목데이터><br>내용: <내용데이터>
        #   위 문자열을 가지고 response돌려주기

        title = request.POST['title']
        text = request.POST['text']

        post = Post.objects.create(
            author=request.user,
            title=title,
            text=text,
        )
        # next_path = reverse('post-list')
        # return HttpResponseRedirect(next_path)

        # URL name으로부터의 reverse과정이 추상화되어있음
        return redirect('post-list')
    else:
        return render(request, 'blog/post_create.html')


def post_update(request, pk):
    if request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']

        post = Post.objects.get(pk=pk)
        # next_path = reverse('post-list')
        # return HttpResponseRedirect(next_path)

        # URL name으로부터의 reverse과정이 추상화되어있음
        return redirect('post-list')
    return render(request, 'blog/post_update.html')
