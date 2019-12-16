from django.shortcuts import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Blog
from .models import BlogType


def blog_list(request):
    context = {
        'blogs': Blog.objects.all(),
        'blogs_count': Blog.objects.all().count(),
    }
    return render(request, 'blog/blog_list.html', context)


def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)  # pk一定是主键，但是id不一定
    context = {
        'blog': blog
    }
    return render(request, 'blog/blog_detail.html', context)


# 模板分类总表
def blogs_type_list(request):
    blog_types = BlogType.objects.all()
    context = {
        'blogs_type_list': blog_types,
    }
    return render(request, 'blog/blog_type_lists.html', context)


# 某个分类的表
def blogs_with_the_same_type(request, blog_type_pk):
    blog_type_from_db = get_object_or_404(BlogType, pk=blog_type_pk)

    context = {
        'blog_type': blog_type_from_db,
        'blogs': Blog.objects.filter(blog_type=blog_type_from_db),
    }
    # return HttpResponse(Blog.objects.filter(blog_type=1))
    return render(request, 'blog/blogs_with_the_same_type.html', context)
