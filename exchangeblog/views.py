from django.shortcuts import render, get_object_or_404
from exchangeblog.models import BlogPost, BlogAuthor
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.contrib.auth.models import Permission
from django.views import generic
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import permission_required
from django.core.exceptions import ValidationError
from uuslug import slugify
import datetime
from django.forms import ModelForm, DateField
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from exchangeblog.filters import BlogPostFilter
from django_filters.views import FilterView

# Create your views here.
class HomePageView(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_blog_posts'] = BlogPost.objects.all().count()
        context['num_blog_authors'] = BlogAuthor.objects.all().count()
        context['latest_posts'] = BlogPost.objects.all()[:3]
        return context

class AboutPageView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_blog_posts'] = BlogPost.objects.all().count()
        context['num_blog_authors'] = BlogAuthor.objects.all().count()
        return context


class BlogPostListView(FilterView):
    model = BlogPost
    filterset_class = BlogPostFilter
    order_by = ['-date_of_creation'] 
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.copy()
        if 'page' in query:
            del query['page']
        context['querystring'] = query.urlencode()
        context['posts_filtered'] = BlogPostFilter(self.request.GET, queryset=self.get_queryset())
        return context

class BlogPostDetailView(generic.DetailView):
    model = BlogPost

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_author = self.get_object().author
        context['num_authors_posts'] = BlogPost.objects.filter(author=current_author).count()
        context['more_posts_from_author'] = BlogPost.objects.filter(author=current_author).exclude(slug=self.get_object().slug)[:2]
        context['next_post'] = BlogPost.objects.filter(date_of_creation__gt=self.get_object().date_of_creation).order_by('date_of_creation')[0:1]
        return context

class BlogAuthorListView(generic.ListView):
    model = BlogAuthor
    paginate_by = 10

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
    fields = ['title', 'date_of_creation', 'language', 'country', 'short_description', 'blogcontent', 'thumbnail_picture'] 
    permission_object = None
    permission_required = 'exchangeblog.add_blogpost'
    permission_denied_message = "Please make sure you're logged in and have applied as an author"
    def form_valid(self, form):
        form.instance.author = get_object_or_404(BlogAuthor, user=self.request.user)
        form.instance.slug = slugify(form.instance.title, stopwords=['a', 'an', 'the', 'to', 'and', 'for'])
        max_posts = get_object_or_404(BlogAuthor, user=self.request.user).allowed_posts
        if BlogPost.objects.filter(author=form.instance.author).count() >= max_posts:
            raise ValidationError(_("You are not allowed to write more than {} posts").format(max_posts))
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