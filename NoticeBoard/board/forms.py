from django import forms
from django.core.exceptions import ValidationError
from .models import Reply, Article


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = [
            'text',
        ]


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'title',
            'category',
            'text',
        ]
