"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.contrib.sitemaps.views import sitemap
from django.utils.translation import gettext_lazy as _
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import permission_required
from django.views.decorators.cache import never_cache
from exchangeblog.views import AboutPageView, HomePageView, PrivacyPolicyView
from blog.sitemaps import PostSiteMap, AuthorSiteMap, StaticViewSitemap
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

sitemaps = {
    'posts': PostSiteMap,
    'authors': AuthorSiteMap,
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('accounts/', include('authentication.urls')),
    #path('accounts/', include('django.contrib.auth.urls')),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
     name='sitemap'),

    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('favicons/favicon.ico'))),
    path('browserconfig.xml', RedirectView.as_view(url=staticfiles_storage.url('favicons/browserconfig.xml'))),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    path('', HomePageView.as_view(), name='home'),
    path(_('about'), AboutPageView.as_view(), name='about'),
    path(_('privacy-policy'), PrivacyPolicyView.as_view(), name="privacy-policy"),
    path(_('blog/'), include('exchangeblog.urls')),
    path(_('guide/'), include('exchangeguide.urls')),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
