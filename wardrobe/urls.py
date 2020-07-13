"""wardrobe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from django.conf.urls import url
from django.contrib import admin
from . import views,testdb,search

urlpatterns = [
    url(r'^runoob$', views.runoob),
    url(r'^testdb$', testdb.testdb),
    url(r'^showdb$', testdb.showdb),
    url(r'^updatedb$', testdb.updatedb),
    path('destroydb/', testdb.destroydb),
    url(r'^search-form$', search.search_form),
    url(r'^search$', search.search),
    url(r'^search-post$', search.search_post),
    path("backend/", include("backend.urls")),
    url(r'^admin/', admin.site.urls),
    path("forground/", include("forground.urls")),
]