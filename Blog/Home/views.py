from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Category, Post


class HomeView(TemplateView):
    template_name = "home/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorys'] = Category.objects.all()
        context['posts'] = Post.objects.all()
        return context
