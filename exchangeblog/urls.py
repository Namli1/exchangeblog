from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.BlogPostListView.as_view(), name='post-list'),
    path('post/<int:pk>', views.BlogPostDetailView.as_view(), name='post-detail'),
    path('authors/', views.BlogAuthorListView.as_view(), name='author-list'),
    path('author/<int:pk>', views.BlogAuthorDetailView.as_view(), name='author-detail'),
    path('post/create', views.BlogPostCreate.as_view(), name='post-create'),
    path('author/create', views.BlogAuthorCreate.as_view(), name='author-create'),
]