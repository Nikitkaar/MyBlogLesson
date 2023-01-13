from django.urls import path
from blog.templates.articles import ArticleDetailView, ArticleListView

urlpatterns = [
    path('', ArticleListView.as_view(), name='articles'),
    path('<slug:slug>/', ArticleDetailView.as_view(), name='article-detail')
]