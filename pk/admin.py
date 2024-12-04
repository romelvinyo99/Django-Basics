from django.contrib import admin
from pk.models import Author, Books


admin.site.register(Books)
admin.site.register(Author)