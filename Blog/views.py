from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from Blog.models import Article
from Blog.forms import ArticleModelForm
from django.urls import reverse


# List View
class ArticleListView(ListView):
    template_name = "articles/article_list.html"
    queryset = Article.objects.all()


# Detail View
class ArticleDetailView(DetailView):
    template_name = "articles/article_detail.html"

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Article, id=id_)


# Create View
class ArticleCreateView(CreateView):
    template_name = "articles/article_create.html"
    form_class = ArticleModelForm
    queryset = Article.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


# Update view
class ArticleUpdateView(UpdateView):
    template_name = "articles/article_create.html"
    form_class = ArticleModelForm
    queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Article, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


# Delete view
class ArticleDeleteView(DeleteView):
    template_name = "articles/article_delete.html"

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return reverse("articles:article-list")
