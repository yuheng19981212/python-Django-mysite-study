from django.urls import path

from . import views

urlpatterns = [
    # http://localhost:8000/blog/1
    path('<int:blog_id>', views.blog_detail, name='article_detail'),
    path('', views.blog_list, name='blog_list'),
    path('type/<int:blog_type_pk>', views.blogs_with_the_same_type, name='blogs_with_the_same_type'),
    path('type/', views.blogs_type_list, name='blogs_type_list')
]
