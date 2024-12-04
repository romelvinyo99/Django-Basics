from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Authors"
        ordering = ("name",)

    def __str__(self):
        return self.name


class Books(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        ordering = ("title",)
        verbose_name_plural = "Books"

    def __str__(self):
        return self.title


"""
--> This is how we will be creating the objects --> many to one relation 
--> when an the root object (author) is deleted all its relational objects are also deleted
--> Nb//: When passing the the root to the relational object we need to make them as instances
author = Author.objects.create(name="Ngugi")
book = Author.objects.create(title="Chozi la Heri", author=author)
"""

"""


"""
