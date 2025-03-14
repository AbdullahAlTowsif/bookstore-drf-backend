from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

# Create a router and register our ViewSets with it.
# router = DefaultRouter()
# router.register(r'books', views.BookListView, basename='book')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    # Method 1 url
    # path('books/', views.BookListView.as_view()), # handle get and post requset
    # path('books/<int:pk>/', views.BookListUpdateDelete.as_view()),
    # Method 2 url
    path('books/', views.BookListCreateAPIView.as_view()), # handle get and post requset
    path('books/<int:pk>/', views.BookRetrieveUpdateDestroyAPIView.as_view()),
]