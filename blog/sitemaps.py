from django.contrib.sitemaps import Sitemap
from exchangeblog.models import BlogAuthor, BlogPost
from django.urls import reverse

class PostSiteMap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    i18n = True

    def items(self):
        return BlogPost.objects.all()

    def lastmod(self, obj):
        return obj.date_of_creation

class AuthorSiteMap(Sitemap):
    changefreq = 'monthly'
    priority = 0.6

    def items(self):
        return BlogAuthor.objects.all()

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'yearly'

    def items(self):
        return ['home', 'about']

    def location(self, item):
        return reverse(item)