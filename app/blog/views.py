import os
import random

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.utils import timezone


def post_list(request):
    # # 템플릿을 가져옴
    # template = loader.get_template('blog/post_list.html')
    # # 해당 템플릿을 렌더링
    # context = {
    #
    # }
    # content = template.render(context, request)
    # return HttpResponse(content)

    # render함수
    #   1번째 인수로 자신의 view의 첫 번째 매개변수인 request를 전달
    #   2번째 인수로 템플릿파일의 경로를 전달
    #   3번째 인수(선택)로 dict를 전달
    # -> 템플릿파일의 경로에 있는 HTML을 가져와서 {{ 변수 }}와 같은 부분들에 동적으로 문자열을 생성
    #    생성된 결과를 HttpResponse로 돌려줌, 브라우저는 해당 결과를 받아 사용자에게 보여주게 됨

    # loader.get_template
    # template.render
    # HttpResponse(content)
    context = {
        'pokemon': random.choice(['피카츄', '파이리', '꼬부기'])
    }
    return render(
        request=request,
        template_name='blog/post_list.html',
        context=context,
    )
    # return render(request, 'blog/post_list.html', context)