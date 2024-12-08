from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index),
    path('posts/<int:pk>/', views.post_detail),
    path('category/<slug:category>/', views.category_posts),
]
