from django.contrib import admin

from .models import Article


# 定制管理后台
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'is_deleted', 'content', 'created_time', 'last_updated_time')  # 设置显示内容
    ordering = ('id',)  # 按照id升序，若写-id则会倒序
    # ordering = ('-id',) # 这样子写会按照id降序排列，默认也是降序的


# admin.site.register(Article, ArticleAdmin)  可以这样去注册
'''注册article的后台管理,第二个参数可以省略
可以使用
admin.site.register(Article, ArticleAdmin)  
也可以使用修饰器在类前面
@admin.register(Article)进行定制
'''
