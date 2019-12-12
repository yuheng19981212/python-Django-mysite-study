from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>hello,world</h1>'
                        + '<br><a href="/article/">跳转到文章列表</a>')
