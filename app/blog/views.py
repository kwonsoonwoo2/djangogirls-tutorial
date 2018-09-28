import os

from django.http import HttpResponse
from django.template import loader
from django.utils import timezone


def post_list(request):
    # 템플릿을 가져옴
    template = loader.get_template('blog/post_list.html')
    # 해당 템플릿을 렌더링
    context = {}
    content = template.render(context, request)
    return HttpResponse(content)