from django.urls import path
from . import views

urlpatterns = [
    #path('', views.blog, name='home'),
    path('<int:blog_id>', views.detail,name="detail"),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('allList/', views.allList, name='allList'),
]