from django.contrib import admin
from exchangeblog.models import BlogPost, BlogAuthor

# Register your models here.
admin.site.register(BlogPost)

class BlogPostInline(admin.TabularInline):
    model = BlogPost
    extra = 0

@admin.register(BlogAuthor)
class AuthorAdmin(admin.ModelAdmin):
    def post_count(self, obj):
        return obj.blogpost_set.count() + obj.countryguidepost_set.count()
    post_count.short_description = "Posts Count"
    list_display = ('user', 'name', 'post_count')
    inlines = [BlogPostInline]
