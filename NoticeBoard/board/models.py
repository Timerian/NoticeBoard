from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Article(models.Model):
    TYPE = (
        ('tanks', 'Танки'),
        ('heal', 'Хилы'),
        ('dd', 'ДД'),
        ('buyers', 'Торговцы'),
        ('guildmasters', 'Гилдмастера'),
        ('quest', 'Квестгиверы'),
        ('smith', 'Кузнецы'),
        ('tanner', 'Кожевенники'),
        ('potion', 'Зельевары'),
        ('spellmasters', 'Мастера заклинаний')
    )

    title = models.CharField(max_length=100, verbose_name='Заголовок')
    category = models.CharField(max_length=12, choices=TYPE, default='tanks', verbose_name='Категория')
    text = RichTextField(blank=True, null=True, verbose_name='Текст статьи')
    create_date = models.DateField(auto_now_add=True, verbose_name='Дата публикации')

    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор публикации', related_name='articles')

    def __str__(self):
        return f"{self.title} | {self.create_date}"

class Reply(models.Model):
    text = models.TextField(max_length=200, verbose_name='Текст отклика')
    create_date = models.DateField(auto_now_add=True, verbose_name='Дата публикации')
    accepted = models.BooleanField(default=False, null=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор отклика', null=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Статья', null=True, related_name='replies')

    def __str__(self):
        return f"{self.author} | {self.create_date}"