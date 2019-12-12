from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# python的类使用类似于参数列表的形式表示继承
# Article类为了是一个模型类需要继承models.Model
class Article(models.Model):
    # 以下可以看成文章的属性
    title = models.CharField(max_length=30)  # 字符串类型的字段
    content = models.TextField()  # 可能很长的用文本字段

    # 由于前期考虑不周，从这开始是新加的属性 新属性必须设置默认值
    created_time = models.DateTimeField(default=timezone.now)  # 设置创建时间
    '''
    因为时间的特殊性，时间的添加也可以用以下语句来进行
    created_time = models.DateTimeField(auto_now_add=True) 
    设置时间为新增时的时间。如果不是时间属性就乖乖的用default吧
    '''
    last_updated_time = models.DateTimeField(auto_now=True)
    '''
    这个auto_now = True 会使得按当前时间更新数据库
    '''
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=1)
    '''
    这一段用来添加用户，用户需要利用另一个模型进行外键关联。
    但是对于Django来说，用户模型有一个现成的可以直接用
    需要引用文件 django.contrib.auth.models import User
    使用外键进行关联，级联为models.DO_NOTHING 从表对主表无影响
    USER表里面的第一个就是自己，所以默认为1就成
    '''

    is_deleted = models.BooleanField(default=False)
    # 采用逻辑删除而非物理删除
    read_num = models.IntegerField(default=0)
    # 用来存放阅读数


# 修改这个函数可以修改后台界面的标题
def __str__(self):
    return self.title  # 这里设置返回文章的标题
