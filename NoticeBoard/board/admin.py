from django.contrib import admin
from .models import Article, Reply


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'create_date')
    ordering = ('create_date', )
    list_filter = ('author', 'create_date')


@admin.register(Reply)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ('author', 'create_date')
    ordering = ('create_date', )
    list_filter = ('author', 'create_date')
    
    