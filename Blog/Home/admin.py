from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.contrib.admin.sites import AdminSite
from .models import Category, Post, Comment


@admin.register(Category)
class Admin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at',)
    list_filter = ('name',)
    search_fields = ('name', 'created_at', 'updated_at',)
    date_hierarchy = 'created_at'
    ordering = ('created_at', 'updated_at',)


@admin.register(Post)
class Admin(admin.ModelAdmin):
    list_display = ('title', 'description', 'category', 'created_by', 'created_at', 'updated_at',)
    list_filter = ('title', 'description', 'category', 'created_by',)
    search_fields = ('title', 'description', 'category', 'created_by', 'created_at',)
    date_hierarchy = 'created_at'
    ordering = ('created_at', 'updated_at',)


@admin.register(Comment)
class Admin(admin.ModelAdmin):
    list_display = ('title', 'content', 'post', 'created_by', 'created_at',)
    list_filter = ('created_by',)
    search_fields = ('title', 'category', 'created_by', 'created_at',)
    date_hierarchy = 'created_at'
    ordering = ('created_at',)