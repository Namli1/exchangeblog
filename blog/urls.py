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
from ckeditor_uploader import views as ckeditor_views
from exchangeblog.views import AboutPageView
from blog.sitemaps import PostSiteMap, AuthorSiteMap, StaticViewSitemap

sitemaps = {
    'posts': PostSiteMap,
    'authors': AuthorSiteMap,
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('accounts/', include('authentication.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('ckeditor/upload/', permission_required('exchangeblog.add_blogpost')(ckeditor_views.upload), name='ckeditor_upload'),
    path('ckeditor/browse/', permission_required('exchangeblog.add_blogpost')(ckeditor_views.browse), name='ckeditor_browse'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
     name='sitemap')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.views.generic import RedirectView

urlpatterns += i18n_patterns(
    path(_('about'), AboutPageView.as_view(), name='about'),
    path(_('blog/'), include('exchangeblog.urls')),
)

urlpatterns += [
    path('', RedirectView.as_view(url='/blog/', permanent=True)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
