from django.contrib import admin
from exchangeblog.models import BlogPost, BlogAuthor

# Register your models here.
admin.site.register(BlogPost)

class BlogPostInline(admin.TabularInline):
    model = BlogPost
    extra = 0

@admin.register(BlogAuthor)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'name',)
    inlines = [BlogPostInline]
