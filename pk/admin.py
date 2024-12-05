from django.contrib import admin
from pk.models import Author, Books,  ImagesModels


admin.site.register(Books)
admin.site.register(Author)
admin.site.register(ImagesModels)