from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    path('about/', views.aboutб name='about'),
    path('rules/', views.rules, name='rules'),
]
