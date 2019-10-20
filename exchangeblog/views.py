from django.shortcuts import render, get_object_or_404
from exchangeblog.models import BlogPost, BlogAuthor
from django.views import generic
from django.contrib.auth.decorators import permission_required

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

class BlogAuthorCreate(generic.CreateView):
    model = BlogAuthor
    fields = ['name', 'bio']

class BlogPostCreate(generic.CreateView):
    model = BlogPost
    fields = ['title', 'language', 'country', 'blogcontent']
    permission_required = 'exchangeblog.can_create_post'
    permission_denied_message = "Please make sure you're logged in and have applied as an author"
    def form_valid(self, form):
        form.instance.author = BlogAuthor.objects.get_object_or_404(user=self.request.user)
