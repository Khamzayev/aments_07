from django.urls import path
from blog.views import  Index,Blog,BlogDetail

app_name = 'blog'

urlpatterns = [    
    path("index/", Index.as_view()),
    path("", Blog.as_view(), name='blog'), #blog/1/blog_detail
    path("<int:pk>/blog_detail/", BlogDetail.as_view(), name='blog_detail'),
]