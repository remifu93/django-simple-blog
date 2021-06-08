from typing import List
from django.http import request
from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import FormMixin
from .models import Category, Post, Comment
from .forms import CommentForm


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


class HomeDetailView(FormMixin, DetailView):
    model = Post
    template_name = "home/post_detail.html"
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['comments'] = self.object.comment_set.all()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()        
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.post = self.object
        obj.created_by = self.request.user
        obj.save()
        return super().form_valid(form)

    def get_success_url(self):
        return self.request.path

