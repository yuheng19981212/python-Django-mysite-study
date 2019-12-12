from django.shortcuts import get_object_or_404  # 获取对象的简便方法
from django.shortcuts import render  # render可以把对象传给其它页面

from .models import Article  # 引用过来模型


# 模型的objects是获取或操作模型的对象
# Article.objects.get(条件)
# Article.objects.all()
# Article.objects.filter（条件）

# 一般麻烦的写法
# def article_detail(request, article_id):
#     try:
#         article = Article.objects.get(id=article_id)
#         '''
#         也可以写成 article = getobject_or_404(Article,pk = article_id)然后取消掉try_except结构
#         '''
#         context = {'article_obj': article}
#         return render(request, 'article_detail.html', context)
#     except Article.DoesNotExist:
#         raise Http404('页面走丢啦')  # 创造404
#         # 还可以这样写 return HttpResponse('页面不存在')

# 这个是获取文章详情
def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    context = {
        'article_obj': article
    }
    return render(request, 'article_detail.html', context)


def article_list(request):
    # articles = Article.objects.all()  # 这个是获取全部文章的写法
    articles = Article.objects.filter(is_deleted=False)  # 获取没有被逻辑删除的目录
    context = {
        'articles': articles
    }
    return render(request, 'article_list.html', context)
