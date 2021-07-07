from django.urls import path
from . import views
from exchangeblog.views import HomePageView
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    path('all/', views.GuidePostListView.as_view(), name="guide-list"),
    path('post/<slug:slug>/', views.GuidePostDetailView.as_view(), name='guide-detail'),
    path('create/', views.GuidePostCreate.as_view(), name="guide-create"),
    path('post/<slug:slug>/update/', views.GuidePostUpdate.as_view(), name="guide-update"),
    path('post/<slug:slug>/delete/', views.GuidePostDelete.as_view(), name="guide-delete"),
    path('countries/', views.CountryGuideListView.as_view(), name="countryguide-list"),
    path('country/<slug:slug>/', views.CountryGuidePostDetailView.as_view(), name="countryguide-detail"),
    path('country/create', views.CountryGuidePostCreate.as_view(), name='countryguide-create'),
    path('country/<slug:slug>/update', views.CountryGuidePostUpdate.as_view(), name='countryguide-update'),
    path('country/<slug:slug>/delete', views.CountryGuidePostDelete.as_view(), name='countryguide-delete'),
]