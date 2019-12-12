from django.urls import path

from . import views

# 此时的路由主地址:local:8000/article/
urlpatterns = [
    path('<int:article_id>', views.article_detail, name='article_detail'),
    path('', views.article_list, name='article_list')
]
