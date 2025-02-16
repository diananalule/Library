from audioop import add
from django.urls import URLPattern, path
from . import views


urlpatterns = [
    path('catalog/<str:user_id>/', views.Books, name='catalog'),
    path('searchbooks', views.searchBooks, name="searchbooks"),
    path('addbook', views.addbookurl, name="addbook"),
    path('addBook', views.addBook, name="addBook"),
    path('borrowbook/<str:book_id>/', views.borrowBook, name="borrowbook"),
    path('deletebook/<str:book_id>/', views.deleteBook, name="deletebook"),
    path('returnbook/<str:book_id>/', views.returnBook, name="returnbook"),
    path('notifications', views.notifications, name='notifications'),

]