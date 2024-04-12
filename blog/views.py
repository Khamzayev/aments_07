from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, TemplateView
from blog.models import  Author, Post
from django.urls import reverse
from blog.forms import CommentForm
from typing import Any
from django.db.models.query import QuerySet
from django.db.models import Count
from django.shortcuts import get_object_or_404



class Blog(ListView):
    queryset = Post.objects.order_by("-id")
    template_name = 'blog/blog.html'


class Index(TemplateView):
    template_name = 'layouts/base.html'  

class BlogDetail(DetailView):
    model = Post
    template_name = 'blog/blog-detail.html'  

    def get_queryset(self) -> QuerySet[Any]:
        qs = Post.objects.order_by("-id")
        tag = self.request.GET.get("tag")
        if tag:
            qs = qs.filter(tag__name=tag)
        return qs
      
