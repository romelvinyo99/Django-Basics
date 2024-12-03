from Blog.views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView
from django.urls import path

app_name = "articles"
urlpatterns = [
    # Default (list view) path url
    path("", ArticleListView.as_view(), name="article-list"),
    path("create/", ArticleCreateView.as_view(), name="article-create"),
    path("<int:pk>/", ArticleDetailView.as_view(), name="article-detail"),
    path("<int:pk>/update/", ArticleUpdateView.as_view(), name="article-update"),
    path("<int:pk>/delete/", ArticleDeleteView.as_view(), name="article-delete")
]
