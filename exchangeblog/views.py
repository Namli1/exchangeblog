from django.shortcuts import render
from exchangeblog.models import BlogPost, BlogAuthor, BlogPostImage
from django.views import generic

# Create your views here.
def home(request):
    """View function for home page of the blog"""

    num_blog_posts = BlogPost.objects.all().count()

    context = {
        'num_blog_posts' : num_blog_posts,
        "home_active" : "active",
    }

    return render(request, 'home.html', context=context)


class BlogPostListView(generic.ListView):
    model = BlogPost
    paginate_by = 20

class BlogPostDetailView(generic.DetailView):
    model = BlogPost

class BlogAuthorListView(generic.ListView):
    model = BlogAuthor
    paginate_by = 5

class BlogAuthorDetailView(generic.DetailView):
    model = BlogAuthor
