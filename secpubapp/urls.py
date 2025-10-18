from django.urls import path
from . import views
from .views import create_user

urlpatterns = [
    path('', views.login_user, name='login'),
    path('add/', views.add_book, name='add_book'),
    path('books/', views.book_list, name='book_list'),
    path('create_user/', views.create_user, name='create_user'),
    path('delete/<int:pk>/', views.delete_book, name='delete_book'),
    path('edit/<int:pk>/', views.edit_book, name='edit_book'),
]