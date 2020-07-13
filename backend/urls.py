from django.urls import path
from django.conf.urls import url
from backend import views # 从自己的 app 目录引入 views
urlpatterns = [
   url(r'^runoob$', views.runoob),
]