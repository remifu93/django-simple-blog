from django.http import request
from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView, DetailView
from .models import Category, Post


class HomeListView(ListView):
    template_name = "home/post_list.html"
    queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        kword = self.request.GET.get("kword")
        category = self.request.GET.get("category")

        if category:
            queryset = Post.objects.filter(category__name=category)
        
        if kword:
            queryset = Post.objects.filter(
                Q(title__icontains=kword) | Q(content__icontains=kword)
            )

        return queryset


class HomeDetailView(DetailView):
    model = Post
    template_name = "home/post_detail.html"

