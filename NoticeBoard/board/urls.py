from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('my_page/', views.myPage, name='my_page'),

    path('<int:id>/', views.articleDetail, name='article_detail'),
    path('article_list/', views.ArticleListView.as_view(), name='article_list'),
    path('article_create/', views.ArticleCreateView.as_view(), name='article_create'),
    path('<int:pk>/article_update/', views.ArticleUpdateView.as_view(), name='article_update'),
    path('<int:id>/article_delete/', views.deleteArticle, name='article_delete'),
    
    path('<int:id>/reply_delete/', views.deleteReply, name='reply_delete'),
    path('<int:id>/reply_accept/', views.acceptReply, name='reply_accept'),
    path('<int:id>/reply_add/', views.addReply, name='reply_add')
]