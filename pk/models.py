from django.db import models


# ----------------------STRAIGHT FORWARD RELATIONSHIP-----------------
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
author = Author.objects.create(name="JK Rowling")
book = Author.objects.create(title="Harry Potter", author=author)

>>> obj = Books.objects.get(id=1) 
>>> obj.author.name
'JK Rowling'
"""


# -----------REVERSE RELATIONSHIP----------------

class AuthorReverse(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Authors"
        ordering = ("name",)

    def __str__(self):
        return self.name


class BooksReverse(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    class Meta:
        ordering = ("title",)
        verbose_name_plural = "Books"

    def __str__(self):
        return self.title


"""
--Step 1: Create an Author instance
author_instance = Author.objects.create(name="Ngugi")

--Step 2: Use the related_name 'books' to create Book instances
author_instance.books.create(title="Chozi la heri")
author_instance.books.create(title="A Grain of Wheat")
"""
