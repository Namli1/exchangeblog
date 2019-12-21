from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.BlogPostListView.as_view(), name='post-list'),
    path('post/create/', views.BlogPostCreate.as_view(), name='post-create'),
    path('<slug:author>/<slug:slug>/', views.BlogPostDetailView.as_view(), name='post-detail'),
    path('authors/', views.BlogAuthorListView.as_view(), name='author-list'),
    path('<slug:slug>', views.BlogAuthorDetailView.as_view(), name='author-detail'),
    path('<slug:author>/<slug:slug>/update/', views.BlogPostUpdate.as_view(), name='post-update'),
    path('<slug:author>/<slug:slug>/delete/', views.BlogPostDelete.as_view(), name='post-delete'),
    path('author/create/', views.BlogAuthorCreate.as_view(), name='author-create'),
]