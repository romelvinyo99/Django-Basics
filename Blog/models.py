from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=200)
    active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("articles:article-detail", kwargs={"pk": self.id})
