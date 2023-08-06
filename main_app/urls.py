from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('comics/', views.comics_index, name='index'),
    path('exclusive/', views.exclusive, name='exclusive'),
    path('comics/create/', views.ComicsCreate.as_view(), name='comics_create'),
    path('comics/<int:comic_id>/', views.comic_detail.as_view(), name='comic_detail'),
    path('hire_me/', views.hire_me, name='hire_me'),
]
