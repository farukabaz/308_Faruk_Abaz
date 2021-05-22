from django.urls import path

from books import views


app_name = 'books'

urlpatterns = [
    path('books/', views.BookListView.as_view(), name="books"),
    path('book/<int:id>/', views.BookDetailsView.as_view(), name="book"),
    path('authors/', views.AuthorListView.as_view(), name="authors"),
    path('author/<int:id>/', views.AuthorDetailsView.as_view(), name="author")
]