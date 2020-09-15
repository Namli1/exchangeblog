from django.urls import path
from . import views
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    path(_('posts/'), views.BlogPostListView.as_view(), name='post-list'),
    path('post/create/', views.BlogPostCreate.as_view(), name='post-create'),
    path('author/create/', views.BlogAuthorCreate.as_view(), name='author-create'),
    path('<slug:slug>/author/update/', views.BlogAuthorUpdate.as_view(), name='author-update'),
    path('<slug:author>/<slug:slug>/', views.BlogPostDetailView.as_view(), name='post-detail'),
    path(_('authors/'), views.BlogAuthorListView.as_view(), name='author-list'),
    path('<slug:slug>', views.BlogAuthorDetailView.as_view(), name='author-detail'),
    path('post/<slug:author>/<slug:slug>/update/', views.BlogPostUpdate.as_view(), name='post-update'),
    path('post/<slug:author>/<slug:slug>/delete/', views.BlogPostDelete.as_view(), name='post-delete'),
]