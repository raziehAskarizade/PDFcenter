from django.urls import path
from . import views

app_name = 'Book'

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('tag/<slug:tag_slug>/', views.book_list, name='book_list_by_tag'),
    path('<int:objectId>/<str:slug>/', views.book_detail, name='book_detail'),
]
