from django.contrib.auth.models import User
from django.db import models


class BlogType(models.Model):
    type_name = models.CharField(max_length=30)
    '''
    博客+博客分类:一对一或者一对多(这里选前者)
    '''

    def __str__(self):
        return self.type_name


class Blog(models.Model):
    title = models.CharField(max_length=50)
    blog_type = models.ForeignKey(BlogType, models.DO_NOTHING)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING,default=1)
    creat_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
