import os

from django.http import HttpResponse
from django.utils import timezone


def post_list(request):
    """
    / (Root URL)에 해당하는 view
    :param request: 실제 HTTP요청에 대한 정보를 가진 객체
    :return:
    """
    cur_path = os.path.abspath(__file__)
    root_dir = os.path.dirname(cur_path)
    template_dir = os.path.join(root_dir, 'templates')
    blog_dir = os.path.join(template_dir, 'blog', 'post_list.html')

    # with문 사용
    with open(blog_dir, 'rt') as f:
        content = f.read()

    # 파일객체 직접 사용 후
    f = open(blog_dir, 'rt')
    content = f.read()
    f.close()

    # 파일객체를 변수에 할당하지 않고 사용
    content = open(blog_dir, 'rt').read()

    return HttpResponse(content)
