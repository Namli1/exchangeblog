from django.shortcuts import render, get_object_or_404
from exchangeblog.models import BlogPost, BlogAuthor
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.contrib.auth.models import Permission
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import permission_required
from django.core.exceptions import ValidationError
from guardian.shortcuts import assign_perm
from uuslug import slugify

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

class BlogAuthorCreate(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    model = BlogAuthor
    fields = ['name', 'bio']
    permission_object = None
    permission_required = "exchangeblog.add_blogauthor"
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.slug = slugify(form.instance.name)
        self.request.user.user_permissions.add(Permission.objects.get(codename="add_blogpost"))
        return super().form_valid(form)

class BlogPostCreate(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    model = BlogPost
    fields = ['title', 'language', 'country', 'blogcontent', 'thumbnail_picture']
    permission_object = None
    permission_required = 'exchangeblog.add_blogpost'
    permission_denied_message = "Please make sure you're logged in and have applied as an author"
    def form_valid(self, form):
        form.instance.author = get_object_or_404(BlogAuthor, user=self.request.user)
        form.instance.slug = slugify(form.instance.title, stopwords=['a', 'the', 'to', 'and'])
        max_posts = get_object_or_404(BlogAuthor, user=self.request.user).allowed_posts
        if BlogPost.objects.filter(author=form.instance.author).count() >= max_posts:
            raise ValidationError("You are not allowed to write more than {} posts".format(max_posts))
        return super().form_valid(form)

class BlogPostUpdate(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = BlogPost
    fields = ['language', 'country', 'blogcontent', 'thumbnail_picture',]

    def test_func(self):
        obj = self.get_object()
        return obj.author == BlogAuthor.objects.get(user=self.request.user)

class BlogPostDelete(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = BlogPost
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return post.author == BlogAuthor.objects.get(user=self.request.user)