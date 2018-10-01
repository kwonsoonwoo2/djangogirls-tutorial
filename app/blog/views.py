import re

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Post


def post_list(request):
    # 1. request.GET에 'page'값이 전달됨
    # 2. 전체 Post QuerySet을 사용해서 Paginator인스턴스를 생성, paginator변수에 할당
    # 3. Paginator인스턴스의 '.page()'메서드를 호출, 호출 인수에 GET요청에 전달된 'page'값을 사용
    # 4. .page()메서드 호출 결과를 cur_posts변수에 할당 (Page Instance)
    # 5. posts변수를 템플릿으로 전달
    # 6. Page Instance는 순회가능한 객체이며, 순회시 각 루프마다 해당 Post Instance를 돌려줌
    #       post_list.html에서 해당 객체를 순회하도록 템플릿을 구현
    # 7. 템플릿에 '이전', '<현재페이지 번호>', '다음' 링크를 생성
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
    post = Post.objects.get(pk=pk)
    # pk에 해당하는 Post Instance를 'post'키 값으로 템플릿에 전달
    if request.method == "POST":
        # form으로부터 전달된 데이터를 변수에 할당
        title = request.POST['title']
        text = request.POST['text']

        # 수정할 Post Instance의 속성에
        # 전달받은 데이터의 값을 할당
        post.title = title
        post.text = text

        # DB에 변경사항을 update
        post.save()

        # /posts/<pk>/
        return redirect('post-detail', pk=pk)
    else:
        context = {
            'post': post,
        }
        return render(request, 'blog/post_update.html', context)
