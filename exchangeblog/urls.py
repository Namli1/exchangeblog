from django.urls import path
from . import views
from exchangeblog.views import HomePageView, AboutPageView
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path(_('posts/'), views.BlogPostListView.as_view(), name='post-list'),
    path(_('post/create/'), views.BlogPostCreate.as_view(), name='post-create'),
    path(_('author/create/'), views.BlogAuthorCreate.as_view(), name='author-create'),
    path('<slug:author>/<slug:slug>/', views.BlogPostDetailView.as_view(), name='post-detail'),
    path(_('authors/'), views.BlogAuthorListView.as_view(), name='author-list'),
    path('<slug:slug>', views.BlogAuthorDetailView.as_view(), name='author-detail'),
    path('<slug:author>/<slug:slug>/update/', views.BlogPostUpdate.as_view(), name='post-update'),
    path('<slug:author>/<slug:slug>/delete/', views.BlogPostDelete.as_view(), name='post-delete'),
]