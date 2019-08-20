from django.contrib import admin
from exchangeblog.models import BlogPost, BlogAuthor, BlogPostImage

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(BlogAuthor)
admin.site.register(BlogPostImage)

