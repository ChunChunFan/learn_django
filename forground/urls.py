from django.urls import path
from django.conf.urls import url
from forground import views # 从自己的 app 目录引入 views
from forground import testform
urlpatterns = [
   path('add_book/', views.add_book),
   url(r'^save_add_book$', views.save_add_book),
   path('save_many_data/', views.save_many_data),
   path('show_many_data/', views.show_many_data),
   path('juhe_select/', views.juhe_select),
   path('add_emp/', testform.add_emp)
]