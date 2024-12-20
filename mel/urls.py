"""
URL configuration for mel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.shortcuts import HttpResponse
from django.conf import settings
from django.conf.urls.static import static


# Defining the default home-view-page
def home_view(request):
    return HttpResponse("<h1>Home Page</h1>")


urlpatterns = [
    path("", home_view, name="home"),
    path('admin/', admin.site.urls),
    path("Blog/", include("Blog.urls", "articles")),
    path("courses/", include("courses.urls", "courses"))
]

# Serving Media files in development

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
