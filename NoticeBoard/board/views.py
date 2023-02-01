from django.shortcuts import render
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView

from django.http.response import HttpResponse, HttpResponseRedirect

from .filters import ReplyFilter

from . import models
from . import forms


def main_page(request):
    context = {}
    return render(request, 'board/main.html', context)


def articleDetail(request, id):
    article = models.Article.objects.get(id=id)
    user = request.user

    if request.method == "POST":
        form = forms.ReplyForm(request.POST)
        if form.is_valid():
            new_reply = form.save(commit=False)
            new_reply.author = user
            new_reply.save()
            return HttpResponseRedirect('/my_page/')
    else:
        form = forms.ReplyForm()

    context = {
        'article': article,
        'form': form
    }

    return render(request, 'board/article/detail.html', context)


def deleteArticle(request, id):
    models.Article.objects.get(id=id).delete()
    return HttpResponseRedirect("/my_page")


class ArticleListView(ListView):
    model = models.Article
    context_object_name = 'articles'
    template_name = 'board/article/list.html'


class ArticleCreateView(CreateView):
    model = models.Article
    form_class = forms.ArticleForm
    template_name = 'board/article/create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse_lazy('my_page')


class ArticleUpdateView(UpdateView):
    model = models.Article
    form_class = forms.ArticleForm
    template_name = 'board/article/update.html'


@login_required
def myPage(request):
    user = request.user
    articles = user.articles.all()
    all_replies = models.Reply.objects.none()

    for article in articles:
        replies = article.replies.all()
        print("replies", replies)
        all_replies |= replies

    print("all_replies", all_replies)

    queryset = all_replies

    filter = ReplyFilter(request.GET, queryset=queryset)

    context = {
        'articles': articles,
        'filter': filter
    }

    return render(request, 'board/my_page.html', context)


def addReply(request, id):
    if request.method == "POST":
        author = request.user
        article = models.Article.objects.get(id=id)

        data = request.POST

        reply = models.Reply.objects.create(
            text=data['text'],
            author=author,
            article=article,
        )

        reply.save()

    return HttpResponseRedirect(f'/{id}')


def acceptReply(request, id):
    reply = models.Reply.objects.get(id=id)
    reply.accepted = True
    reply.save()
    return HttpResponseRedirect("/my_page")


def deleteReply(request, id):
    models.Reply.objects.get(id=id).delete()
    return HttpResponseRedirect("/my_page")