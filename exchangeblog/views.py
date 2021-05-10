from django.shortcuts import render, get_object_or_404
from exchangeblog.models import BlogPost, BlogAuthor
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.contrib.auth.models import Permission
from django.views import generic
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import permission_required
from django.core.exceptions import PermissionDenied
from django.utils.translation import ugettext_lazy as _
from uuslug import slugify
import datetime
from django.forms import ModelForm, DateField
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from exchangeblog.filters import BlogPostFilter
from django_filters.views import FilterView
from exchangeguide.models import GuidePost, CountryGuidePost
from exchangeblog.forms import BlogAuthorCreateForm
from authentication.models import RegistrationCode

# Create your views here.
class HomePageView(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['num_blog_posts'] = BlogPost.objects.all().count()
        # context['num_blog_authors'] = BlogAuthor.objects.all().count()
        context['latest_posts'] = BlogPost.objects.all()[:3]
        context['guide_teaser'] = GuidePost.objects.all()[:3]
        if self.request.user.is_authenticated:
            context['username'] = self.request.user.username
            if self.request.user.has_perm('exchangeblog.add_blogauthor') and not BlogAuthor.objects.filter(user=self.request.user).exists():
                        context['needs_author_registration'] = True
            try:
                if BlogAuthor.objects.get(user=self.request.user):
                    context["author_name"] = BlogAuthor.objects.get(user=self.request.user).slug
            except:
                pass
        return context

class AboutPageView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_blog_posts'] = BlogPost.objects.all().count()
        context['num_blog_authors'] = BlogAuthor.objects.all().count()
        return context

class PrivacyPolicyView(TemplateView):
    template_name = "privacy-policy.html"

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
        if self.request.user.is_authenticated:
            try:
                if BlogAuthor.objects.get(user=self.request.user):
                    context["is_author"] = BlogAuthor.objects.get(user=self.request.user).slug
            except:
                pass
        return context

class BlogPostDetailView(generic.DetailView):
    model = BlogPost

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_author = self.get_object().author
        context['num_authors_posts'] = BlogPost.objects.filter(author=current_author).count()
        context['more_posts_from_author'] = BlogPost.objects.filter(author=current_author).exclude(slug=self.get_object().slug)[:2]
        context['next_post'] = BlogPost.objects.filter(date_of_creation__gt=self.get_object().date_of_creation).order_by('date_of_creation')[0:1]
        post = self.get_object()
        if self.request.user.is_authenticated:
            try:
                if post.author == BlogAuthor.objects.get(user=self.request.user):
                    context["is_author"] = True
            except:
                pass
        return context

class BlogAuthorListView(generic.ListView):
    model = BlogAuthor
    paginate_by = 10

class BlogAuthorDetailView(generic.DetailView):
    model = BlogAuthor

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            try:
                if BlogAuthor.objects.get(user=self.request.user):
                    context["is_current_author"] = True
            except:
                pass
        return context

class BlogAuthorCreate(UserPassesTestMixin, LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    form_class = BlogAuthorCreateForm
    template_name = 'exchangeblog/blogauthor_form.html'
    permission_object = None
    permission_required = "exchangeblog.add_blogauthor"
    permission_denied_message = _('Permission Denied, ask the site admin if you are allowed to become an author. If you are an author already, you also can\'t access this site.')
    
    def test_func(self):
        if self.request.user.is_authenticated:
            try:
                if BlogAuthor.objects.get(user=self.request.user):
                    return False
            except:
                return True
        else:
            return False
    
    def get_form_kwargs(self):
        kwargs = super(BlogAuthorCreate, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.slug = slugify(form.instance.name)
        registration_code = form.cleaned_data.get('registration_code')
        if RegistrationCode.objects.filter(code=registration_code).first().check_if_used_by_this_user(user=self.request.user):
            used_code = RegistrationCode.objects.filter(code=registration_code).first()
            form.instance.allowed_countries = used_code.allowed_countries
            #TODO: Maybe delete the code after having been used here???
            # RegistrationCode.objects.filter(code=registration_code).first().delete()
        self.request.user.user_permissions.add(Permission.objects.get(codename="add_blogpost"))
        return super().form_valid(form)

class BlogAuthorUpdate(UserPassesTestMixin, LoginRequiredMixin, generic.UpdateView):
    model = BlogAuthor
    fields = ['name', 'social_media_link', 'bio']
    permission_denied_message = _("Permission denied. You don't have access to this site.")
    
    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.name)
        return super().form_valid(form)

    def test_func(self):
        try:
            obj = self.get_object()
            return obj == BlogAuthor.objects.get(user=self.request.user)
        except:
            return False

class BlogPostCreate(LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin, generic.CreateView):
    model = BlogPost
    fields = ['title', 'language', 'country', 'short_description', 'blogcontent', 'thumbnail_picture'] 
    permission_object = None
    permission_required = 'exchangeblog.add_blogpost'
    permission_denied_message = _("Please make sure you're logged in and have applied as an author.")
    
    def form_valid(self, form):
        form.instance.date_of_creation = datetime.date.today()
        form.instance.author = get_object_or_404(BlogAuthor, user=self.request.user)
        form.instance.slug = slugify(form.instance.title, stopwords=['a', 'an', 'the', 'to', 'and', 'for'])
        max_posts = get_object_or_404(BlogAuthor, user=self.request.user).allowed_posts
        if CountryGuidePost.objects.filter(author=form.instance.author).count() + BlogPost.objects.filter(author=form.instance.author).count() >= max_posts:
            raise PermissionDenied(_("You are not allowed to write more than {} posts, sorry. Please contact the admin via Instagram to ask if you can write more.").format(max_posts))
        return super().form_valid(form)

    def test_func(self):
        max_posts = get_object_or_404(BlogAuthor, user=self.request.user).allowed_posts
        if CountryGuidePost.objects.filter(author=get_object_or_404(BlogAuthor, user=self.request.user)).count() + BlogPost.objects.filter(author=get_object_or_404(BlogAuthor, user=self.request.user)).count() >= max_posts:
            raise PermissionDenied(_("You are not allowed to write more than {} posts, sorry. Please contact the admin via Instagram to ask if you can write more.").format(max_posts))
        return True
            

class BlogPostUpdate(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = BlogPost
    fields = ['language', 'country', 'short_description', 'blogcontent', 'thumbnail_picture',]

    def test_func(self):
        obj = self.get_object()
        return obj.author == BlogAuthor.objects.get(user=self.request.user)

class BlogPostDelete(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = BlogPost
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return post.author == BlogAuthor.objects.get(user=self.request.user)