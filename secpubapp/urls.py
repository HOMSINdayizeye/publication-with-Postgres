from django.urls import path
from .import views
from django.views.generic import RedirectView

urlpatterns = [
path('', views.login_user, name='login'),
path('', views.add_book, name='add_book'),
path('add/',views.add_book, name='add_book'),
path('', RedirectView.as_view(url='/secpubapp/', permanent=False)),
path('books/', views.book_list, name='book_list'),
 path('delete/<int:pk>/', views.delete_book, name='delete_book'),

]