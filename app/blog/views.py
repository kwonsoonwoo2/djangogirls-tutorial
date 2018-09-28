from django.shortcuts import render

from .models import Post


def post_list(request):
    posts = Post.objects.all()
    content = ''
    content += '<ul>'
    for post in posts:
        content += f'<li>{post.title}</li>'
    content += '</ul>'

    context = {
        'posts': content,
    }
    return render(request, 'blog/post_list.html', context)
